# for HV scan use
# for HV in On Off; do for Q in 12 38; do python makeEffCurve.py --input /home/makovec/ALTIROC2/cadamuro/FastFadaMeasurements/Measurements2ASIC/bumpConnection_FBM-FR-007_Gaetano_17Mag2023_Hv${HV}/thresScan/B_22_On_col_Inj_col_N_20_Q_${Q}/ --module --prefix HV_${HV}_Q_${Q} --output-dir FBM-FR-007_Gaetano/bumpConnection ; done ; done

import pandas as pd
import numpy as np
import os
from functools import partial # for partial formatting
import collections 

def parse_infos(pathname):
    while pathname[-1] == '/': # remove trailing slashes
        pathname = pathname[:-1]
    toks = pathname.split('/')
    fol  = toks[-1]
    tfol = fol.split('_')
    data = {}
    for i in range(0, len(tfol), 2):
        key = tfol[i]
        val = tfol[i+1]
        data[key] = val
    
    measfol = toks[-2]
    measfol.replace('/', '')
    data['measType'] = measfol

    return data

def open_file(fname, newColName=None, newColVal=None):
    df = pd.read_csv(fname)
    if newColName:
        df[newColName] = newColVal
    return df

def open_scan(fname_proto, scanpoints, scanvar='dac', other_repl = {}):
    dflist = []  # one df per scanvar value
    foundserieselem = [] # the scanvar value corresponding to each item in teh list above
    for p in scanpoints:
        repl = dict(other_repl)
        repl[scanvar] = p
        fname = fname_proto.format(**repl)
        # print(fname)
        if not os.path.isfile(fname):
            continue
        # print('[INFO] opening', fname)
        pdf = open_file(fname, scanvar, p)

        # temp hack for asicnumber
        if 'asic' in pdf.columns:
            pdf['asicnumber'] = pdf['asic']
        else:
            pdf['asicnumber'] = 0

        dflist.append(pdf)
        foundserieselem.append(p)
    if dflist:
        df = pd.concat(dflist)
        return df, foundserieselem
    else:
        return None

def open_scan_series(fname_proto, serieslist, scanpoints, seriesvar='col', scanvar='dac', other_repl = {}):
    dflist = []
    repl = dict(other_repl)
    for s in serieslist:
        repl[seriesvar] = s
        sdf, _ = open_scan(fname_proto, scanpoints, scanvar,  other_repl = repl)
        if sdf is not None:
            sdf[seriesvar] = s
            dflist.append(sdf)
    df = pd.concat(dflist)
    return df

def open_scan_series_auto(base_folder, fname_proto, scanpoints, seriesvar='col', scanvar='dac', indexscansby='pixelInj', other_repl = {}):
    """ this loops on all folders inside the base_folder """
    dflist = []
    pointsfound = {}
    all_folders = [f.path for f in os.scandir(base_folder) if f.is_dir()]
    print (f'[INFO] : identified {len(all_folders)} subfolders to analyse')
    print("base_folder: ",base_folder)
    print("fname_proto: ",fname_proto)
    print("all_folders: ",all_folders)
    for fol in all_folders:
        basename = os.path.basename(os.path.normpath(fol))        
        print (' - : ', basename)
        infos = parse_infos(fol)        
        sdf, foundserieselem = open_scan('/'.join([fol, fname_proto]), scanpoints, scanvar, other_repl = other_repl)
        if sdf is not None:
            for k,v in infos.items():
                sdf[k] = v
            dflist.append(sdf)
            thisidx = infos[indexscansby]
            pointsfound[thisidx] = foundserieselem
    df = pd.concat(dflist)
    return df, pointsfound


def count_to_arrs(count):
    # x = []
    # y = []
    l = list(count.items())
    l.sort() # make sure it's ordered by dac increasing values
    x,y = zip(*l)
    x = np.asarray(x, 'float64')
    y = np.asarray(y, 'float64')
    return x, y

def make_curves(df, scanvar='dac', nmax=20):
    eff_curves = {}
    # scanpoints = df[scanvar].unique()

    pixelgroups = df.groupby('pixel')
    for pix, group in pixelgroups:
        eff_curves[pix] = {}
        # eff_curves[pix]['x'] = group[scanvar].unique()
        pixcounts = group['dac'].value_counts(sort=False)
        # eff_curves[pix]['y'] = pixcounts
        x,y = count_to_arrs(pixcounts)
        y = y/nmax
        eff_curves[pix]['x'] = x
        eff_curves[pix]['y'] = y

    return eff_curves
    # print(scanpoints)

##############
##### this fails when there is noisy in non-injected columns (how is it possible though? other pixels should be off)
# def make_curves_with_scanpoints(df, scanpoints, scanindexedby='pixelInj', scanvar='dac', nmax=20):
#     eff_curves = {}
#     pixelgroups = df.groupby('pixel')
#     for pix, group in pixelgroups:
#         eff_curves[pix] = {}
#         pixcounts = group['dac'].value_counts(sort=False)
#         scannedvar = group[scanindexedby].unique()
#         if scannedvar.shape[0] != 1:
#             print('[ERROR] on pixel', pix)
#             print(scannedvar)
#             raise RuntimeError('the selected group of pixels has %i different values of %s as input' % (scannedvar.shape[0], scanindexedby))
#         exp_scanpoints = get_pixel_list(scannedvar[0])
#         for p in exp_scanpoints:
#             if not p in pixcounts:
#                 pixcounts[p] = 0
#         x,y = count_to_arrs(pixcounts)
#         y = y/nmax
#         eff_curves[pix]['x'] = x
#         eff_curves[pix]['y'] = y

#     return eff_curves


###############
##### index by injection, then group by pixels
def make_curves_with_scanpoints(df, scanpoints, scanindexedby='pixelInj', scanvar='dac', nmax=20, ascending=True): 
    eff_curves = {}
    inj_patterns = scanpoints.keys() # e.g. col0, col1, ...
    for ip in inj_patterns:        
        pdf = df[df[scanindexedby] == ip]
        scan_list  = scanpoints[ip]
        exp_pixels = get_pixel_list(ip)      
        for pix in exp_pixels:           
            if pix in eff_curves: # one pixel should be checked only once
                raise RuntimeError('[ERRROR] trying to re-count efficiency of pixel %i' % ep)
            eff_curves[pix] = {}
            pixpdf = pdf[pdf['pixel'] == pix]

            pixcounts = pixpdf[scanvar].value_counts(sort=False)
            for p in scan_list:
                if not p in pixcounts:
                    pixcounts[p] = 0
            x,y = count_to_arrs(pixcounts) # defaults ot increasing dac order
            
            trig_nb = pixpdf.groupby([scanvar])["trigger_nb"].mean()#zhenwu add
            trig_nb = np.array(trig_nb)#zhenwu add
            trig_all = np.zeros(len(y))#zhenwu add
            for i in range(0,len(y)):#zhenwu add
                if i< (len(y)-len(trig_nb)):#zhenwu add
                    trig_all[i] = nmax#zhenwu add
                else:#zhenwu add
                    trig_all[i] = trig_nb[i-(len(y)-len(trig_nb))]#zhenwu add
            
            if not ascending:
               x = np.flip(x)
               y = np.flip(y)
               trig_all = np.flip(trig_all)#zhenwu add
            y = y/nmax
            y = y*nmax/trig_all#zhenwu add

            eff_curves[pix]['x'] = x
            eff_curves[pix]['y'] = y
    return eff_curves


def start_valid_island(a, thresh, window_size):
    # from https://stackoverflow.com/questions/57712650/numpy-array-first-occurence-of-n-consecutive-values-smaller-than-threshold
    m = a<thresh
    me = np.r_[False,m,False]
    idx = np.flatnonzero(me[:-1]!=me[1:])
    lens = idx[1::2]-idx[::2]
    return idx[::2][(lens >= window_size).argmax()]

def get_thresholds(eff_curves, thr=0.5):
    thresholds = {}
    for pix, curve in eff_curves.items():
        if np.sum(curve['y'] < thr) == 0: # no thresholds could be found (all values are > threshol)
            thresholds[pix] = np.nan
        else:
            it = start_valid_island(curve['y'], thr, 3) # require at least 3 points below threshold
            t  =  curve['x'][it] # this is the first value that goes **below** threshold
            thresholds[pix] = t
    return thresholds

def fill_nondef_with(thr_dict, val):
    """ add a threshold of val to each pixel not defined """
    data = {}
    for ipix in range(225):
        if not ipix in thr_dict:
            data[ipix] = val
        else:
            data[ipix] = thr_dict[ipix]

    ## now sort by pixel number, since this is expected downstream
    odict = collections.OrderedDict(sorted(data.items()))
    return odict

def make_vthc_file(foutname, thr_dict, vals_default=128):
    print ("[INFO] generating Vthc file named", foutname)
    f = open(foutname, 'w')
    lproto = "{addr} ,B'{val:08b}\n"
    for ipix in range(225):
        val = thr_dict[ipix] if ipix in thr_dict else vals_default
        if np.isnan(val):
            val = vals_default
        val = int(val)
        # except ValueError:
        #     print (f'vthc file {foutname} : error on pixel {ipix} - value = {val}  -> will force default = {vals_default}')
            # val = int(vals_default)
        f.write(lproto.format(addr=4+16*(16*(ipix//15))+16*(ipix%15), val=val))
 
    f.close()

def get_pixel_list(pixStr):
    if 'col' in pixStr:
        icol = int(pixStr.replace('col', ''))
        return [15*icol + irow for irow in range(15)]
    elif 'row' in pixStr:
        irow = int(pixStr.replace('row', ''))
        return [15*icol + icol for icol in range(15)]
    else:
        return [int(pixStr)]
    raise RuntimeError(f'Could not parse pixStr {pixStr}')

def chargeDac_to_fc(dac):
    if dac <= 63:
        return dac *0.4
    else:
        return dac *1.7

if __name__ == '__main__':

    # python makeEffCurve.py --module --input /home/makovec/ALTIROC2/cadamuro/FastFadaMeasurements/Measurements2ASIC/scan_DigModuleTest_16Feb2023_hvOff/thresScan/B_22_On_col_Inj_col_N_20_Q_12

    # df = open_scan(
    #     '/Users/Luca/Downloads/FastFadaMeasurements/scan_ThermCycle_restarted_-30_30_3Feb2022_step6_hvOn/thresScan/B_22_On_col_Inj_col_N_20_Vth_0_Q_25/pixelOn_col3_pixelInj_col3/timing_data_dacVth_{dac}_.csv',
    #     scanpoints,
    #     'dac'
    # )
    # fproto = '/Users/Luca/Downloads/FastFadaMeasurements/scan_ThermCycle_restarted_-30_30_3Feb2022_step6_hvOn/thresScan/B_22_On_col_Inj_col_N_20_Vth_0_Q_25/pixelOn_{col}_pixelInj_{col}/timing_data_dacVth_{dac}_.csv'
    # import sys
    # if len(sys.argv) < 2:
    #     raise RuntimeError("usage : python makeEffCurve.py path/to/folder")

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',  help='input folder', required=True)
    parser.add_argument('--module', help='this is a module - read two asics (default : 1 asic)', default=False, action='store_true')
    parser.add_argument('--output-curve',  help='output name for curves',    default='threshold_scan.pdf')
    parser.add_argument('--output-maps',   help='output name for 2d map',    default='threshold_map.pdf')
    parser.add_argument('--output-txt',    help='output name for txt file',  default='threshold_list.txt')
    parser.add_argument('--output-csv',    help='output name for csv file',  default='threshold_list.csv')
    parser.add_argument('--output-meta',   help='output name for metadata file',  default='metadata.txt')
    parser.add_argument('--output-vthc',   help='output name for vthc file (only if this is a vthc measurement) - code adds asic0, asic1 in front', default='vthc.txt')
    parser.add_argument('--prefix-output', help='prefix this string followde by _ to all output names', default=None)
    parser.add_argument('--output-dir',    help='output directory (prepend this + / to all output names)', default=None)
    parser.add_argument('--xrange0',       help='user defined x range for scan curves ASIC 0 (pass xmin, xmax)', nargs=2, default=None, type=float)
    parser.add_argument('--xrange1',       help='user defined x range for scan curves ASIC 1 (pass xmin, xmax)', nargs=2, default=None, type=float)
    parser.add_argument('--doOnly',        help='list of things to restrict in analysis (done at the df level). Pass a list of colX, rowX, or pixel numbers', nargs='+', default=None)
    args = parser.parse_args()
    infos = parse_infos(args.input)
    print(f'[INFO] Deduced properties :')
    print(f'       - meas type       : {infos["measType"]}')
    if 'Q' in infos:
        print(f'       - Q (inj. charge) : {infos["Q"]}')
    print(f'       - N (num. trig)   : {infos["N"]}')
    # print(f'       - On              : {infos["On"]}')
    # print(f'       - Inj             : {infos["Inj"]}')

    # inj_str = {
    #     'col'   : '{col}',
    #     'allTZ' : 'allTZ'
    # }

    # descending_fol_names = 'pixelOn_%s_pixelInj_%s' % (inj_str[infos["On"]], inj_str[infos["Inj"]])

    # # scanpoints determined the dac lookup order and so the order of the curves
    # # threshold finding algorithms expect the points to go from low to high
    # if infos['measType'] == 'thresScan':
    #     scanpoints = list(range(0, 1024))  ## increasing Vth -> reducing eff
    #     timing_fname = 'timing_data_dacVth_{dac}_.csv'
    #     # fproto = '%s/pixelOn_{col}_pixelInj_{col}/timing_data_dacVth_{dac}_.csv' % args.input ## fixme: deduce from name
    #     # fproto = '%s/pixelOn_allTZ_pixelInj_{col}/timing_data_dacVth_{dac}_.csv' % args.input
    #     # fproto = '%s/pixelOn_%s_pixelInj_%s/timing_data_dacVth_{dac}_.csv' % (args.input, inj_str[infos["pixelOn"]], inj_str[infos["pixelInj"]])
    # elif infos['measType'] == 'vthcScan':
    #     scanpoints = list(reversed(range(0, 256))) ## reducing Vth -> reducing eff
    #     timing_fname = 'timing_data_dacVthc_{dac}_.csv'
    #     # fproto = '%s/pixelOn_{col}_pixelInj_{col}/timing_data_dacVthc_{dac}_.csv' % args.input
    # elif infos['measType'] == 'chargeScan':
    #     scanpoints = list(reversed(range(0, 128))) ## reducing charge -> reducing eff
    #     timing_fname = 'timing_data_dacCharge_{dac}_.csv'
    #     # fproto = '%s/pixelOn_{col}_pixelInj_{col}/timing_data_dacCharge_{dac}_.csv' % args.input ## fixme: deduce from name
    #     # fproto = '%s/pixelOn_allTZ_pixelInj_{col}/timing_data_dacCharge_{dac}_.csv' % args.input ## fixme: deduce from name
    # else:
    #     raise RuntimeError("measurement type %s not understood, cannot guess scanpoints" % infos['measType'])

    # fproto = '/'.join([args.input, descending_fol_names, timing_fname])
    # print(fproto)


    # # scanpoints determined the dac lookup order and so the order of the curves
    # # threshold finding algorithms expect the points to go from low to high
    # if infos['measType'] == 'thresScan':
    #     scanpoints = list(range(0, 1024))  ## increasing Vth -> reducing eff
    #     # timing_fname = 'timing_data_dacVth_{dac}_.csv'
    #     fproto = '%s/pixelOn_{col}_pixelInj_{col}/timing_data_dacVth_{dac}_.csv' % args.input ## fixme: deduce from name
    #     # fproto = '%s/pixelOn_allTZ_pixelInj_{col}/timing_data_dacVth_{dac}_.csv' % args.input
    #     # fproto = '%s/pixelOn_%s_pixelInj_%s/timing_data_dacVth_{dac}_.csv' % (args.input, inj_str[infos["pixelOn"]], inj_str[infos["pixelInj"]])
    # elif infos['measType'] == 'vthcScan':
    #     scanpoints = list(reversed(range(0, 256))) ## reducing Vth -> reducing eff
    #     # timing_fname = 'timing_data_dacVthc_{dac}_.csv'
    #     fproto = '%s/pixelOn_{col}_pixelInj_{col}/timing_data_dacVthc_{dac}_.csv' % args.input
    # elif infos['measType'] == 'chargeScan':
    #     scanpoints = list(reversed(range(0, 128))) ## reducing charge -> reducing eff
    #     # timing_fname = 'timing_data_dacCharge_{dac}_.csv'
    #     fproto = '%s/pixelOn_{col}_pixelInj_{col}/timing_data_dacCharge_{dac}_.csv' % args.input ## fixme: deduce from name
    #     # fproto = '%s/pixelOn_allTZ_pixelInj_{col}/timing_data_dacCharge_{dac}_.csv' % args.input ## fixme: deduce from name
    # else:
    #     raise RuntimeError("measurement type %s not understood, cannot guess scanpoints" % infos['measType'])



    # fproto = '/'.join([args.input, descending_fol_names, timing_fname])
    # print(fproto)

    # fproto = '/home/makovec/ALTIROC2/cadamuro/FastFadaMeasurements/scan_ThermCycle_-30_30_3Feb2022_step1_hvOn/thresScan/B_22_On_col_Inj_col_N_20_Vth_0_Q_25/pixelOn_{col}_pixelInj_{col}/timing_data_dacVth_{dac}_.csv'
    # fproto = '%s/pixelOn_{col}_pixelInj_{col}/timing_data_dacVth_{dac}_.csv' % sys.argv[1]
    # collist = ['col{}'.format(i) for i in range(15)]

    # df = open_scan_series(
    #     fproto,
    #     collist,
    #     scanpoints,
    # )

    if infos['measType'] == 'thresScan':
        scanpoints = list(range(0, 1024))  ## increasing Vth -> reducing eff
        timing_fname = 'timing_data_dacVth_{dac}_.csv'
        ascending=True
    elif infos['measType'] == 'vthcScan':
        scanpoints = list(reversed(range(0, 256))) ## reducing Vth -> reducing eff
        timing_fname = 'timing_data_dacVthc_{dac}_.csv'
        ascending=False
    elif infos['measType'] == 'chargeScan':
        scanpoints = list(reversed(range(0, 128))) ## reducing charge -> reducing eff
        timing_fname = 'timing_data_dacCharge_{dac}_.csv'
        ascending=False
    else:
        raise RuntimeError("measurement type %s not understood, cannot guess scanpoints" % infos['measType'])


    df, folderdictscanpoints = open_scan_series_auto(
        args.input,
        timing_fname,
        scanpoints
    )

    if args.doOnly:
        print('[INFO] Restricting to', args.doOnly)
        toplot = []
        for todo in args.doOnly:
            toplot += get_pixel_list(todo)
        toplot = sorted(list(set(toplot))) # make unique, and sort
        print('[INFO] Will filter to the following pixels: ', toplot)
        df = df[df.pixel.isin(toplot)]

    ## ec [pixel]['x'/'y']
    if not args.module:
        # ec = make_curves(df, nmax=int(infos['N']))
        ec = make_curves_with_scanpoints(df, folderdictscanpoints, nmax=int(infos['N']), ascending=ascending)
        thr = get_thresholds(ec)
        ec  = {0 : ec}
        thr = {0 : thr}
    else:
        # ec0 = make_curves(df[df.asicnumber == 0], nmax=int(infos['N'])) 
        ec0 = make_curves_with_scanpoints(df[df.asicnumber == 0], folderdictscanpoints, nmax=int(infos['N']), ascending=ascending)
        thr0 = get_thresholds(ec0)
        # ec1 = make_curves(df[df.asicnumber == 1], nmax=int(infos['N']))
        ec1 = make_curves_with_scanpoints(df[df.asicnumber == 1], folderdictscanpoints, nmax=int(infos['N']), ascending=ascending)
        thr1 = get_thresholds(ec1)
        ec = {0 : ec0, 1 : ec1}
        thr = {0 : thr0, 1 : thr1}

    import matplotlib
    import matplotlib.pyplot as plt
    if not args.module:
        fig_crv, axs_crv = plt.subplots()
        fig_map, axs_map = plt.subplots()
        axs_crv = [axs_crv,]
        axs_map = [axs_map,]
        nasic = 1
    else:
        fig_crv, axs_crv = plt.subplots(2,1)
        fig_map, axs_map = plt.subplots(1,2,figsize=(20, 10))
        nasic = 2

    xranges = [args.xrange0, args.xrange1]

    for iasic in range(nasic):
        pixlist = ec[iasic].keys()
        for pix in pixlist:
            axs_crv[iasic].plot(ec[iasic][pix]['x'], ec[iasic][pix]['y'], label=str(pix))
        axs_crv[iasic].set_title(f'ASIC {iasic}')
        axs_crv[iasic].set_xlabel('DAC')
        axs_crv[iasic].set_ylabel('Efficiency')
        if xranges[iasic]:
            axs_crv[iasic].set_xlim(xranges[iasic][0], xranges[iasic][1])
        if args.doOnly:
            # legends = [c for c in axs_crv[iasic].get_children() if isinstance(c, matplotlib.legend.Legend)]
            # axs_crv[iasic].legend(loc='best', ncol=len(legends)//4)
            axs_crv[iasic].legend(loc='best', ncol=3)

        df_thr = pd.DataFrame({'pixel' : list(thr[iasic].keys()), 'thr' : list(thr[iasic].values())})
        thr[iasic] = fill_nondef_with(thr[iasic], np.nan)
        thrdata = np.asarray(list(thr[iasic].values()))
        thrdata = np.reshape(thrdata, (15,15))
        thrdata = thrdata.T
        axs_map[iasic].imshow(thrdata, alpha=0.8, cmap='rainbow', origin='lower')
        # Loop over data dimensions and create text annotations.
        for i in range(15):
            for j in range(15):
                text = axs_map[iasic].text(j, i, thrdata[i, j],
                               ha="center", va="center", color="black")
        

        median    = df_thr['thr'].median()
        median_PA = df_thr[df_thr.pixel <= 119]['thr'].median()
        median_TZ = df_thr[df_thr.pixel >= 120]['thr'].median()
        # axs_map[iasic].set_title(f'ASIC {iasic} \n Median {median:.0f} (VPA: {median_PA:.0f} , TZ: {median_TZ:.0f})')
        # axs_map[iasic].set_title(f'ASIC {iasic} - Median {median:.0f} (VPA: {median_PA:.0f} , TZ: {median_TZ:.0f})')
        axs_map[iasic].set_title(f'ASIC {iasic} - Median {median:.0f}')
        axs_map[iasic].set_xlabel('Column')
        axs_map[iasic].set_ylabel('Row')
        # axs_map[iasic].set_xticks(list(range(0, 15, 2)))
        # axs_map[iasic].set_yticks(list(range(0, 15, 2)))
        axs_map[iasic].set_xticks(list(range(0, 15, 1)))
        axs_map[iasic].set_yticks(list(range(0, 15, 1)))

    # print (thr)
    # fout = open('thr_py.txt', 'w')
    # for pix, th in thr.items():
    #     fout.write('{} {:.0f}\n'.format(pix, th))

    import matplotlib.pyplot as plt
    plt.ion()

    pref_string = infos['measType'] + '_'
    if args.prefix_output :
        pref_string  = pref_string + args.prefix_output + '_'
    if args.output_dir:
        pref_string = args.output_dir + '/' + pref_string

    fig_crv.tight_layout()
    fig_crv.savefig(pref_string + args.output_curve)
    
    fig_map.tight_layout()
    fig_map.savefig(pref_string + args.output_maps)

    ## save thresholds to txt file
    fout = open(pref_string + args.output_txt, 'w')
    for iasic in range(nasic):
        fout.write(f'ASIC {iasic}\n')
        pixlist = ec[iasic].keys()
        for pix in pixlist:
            fout.write(f'{pix:<3} {thr[iasic][pix]}\n')
        fout.write('\n')

    ## make a CSV file
    fcsvname = pref_string + args.output_csv
    d_pixel  = []
    d_thr    = []
    d_asic   = []
    for iasic in range(nasic):
        thispix = thr[iasic].keys()
        d_pixel += list(thispix)
        d_thr   += list(thr[iasic].values())
        d_asic  += [iasic] * len(thispix)

    df = pd.DataFrame({
        'pixel'     : d_pixel,           
        'threshold' : d_thr,
        'asic'      : d_asic
    })
    df.to_csv(fcsvname)

    ## make a vthc file if this is this type of measurement
    if infos['measType'] == 'vthcScan':
        for iasic in range(nasic):
            foutname = f'asic{iasic}_{args.output_vthc}'
            if args.output_dir :
                foutname = args.output_dir + '/' + foutname
            make_vthc_file(foutname, thr[iasic], 128)

    ## save all metadata


    # plt.savefig(args.output)
    from datetime import datetime
    fmetaname = pref_string + args.output_meta
    with open(fmetaname, 'w') as fmeta:
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        fmeta.write("date and time : {}\n".format(dt_string))
        for argname in vars(args):
            fmeta.write('{} : {}\n'.format(argname, getattr(args, argname)))        

