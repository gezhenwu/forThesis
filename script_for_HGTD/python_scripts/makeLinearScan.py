import makeEffCurve as mef
import numpy as np

def make_avg_df(df, scanpoints, vartoavg='tot' , scanindexedby='pixelInj', scannedvar='dac'):
    lin_curves = {}
    inj_patterns = scanpoints.keys() # e.g. col0, col1, ...
    for ip in inj_patterns:
        pdf = df[df[scanindexedby] == ip]
        scan_list  = scanpoints[ip]
        exp_pixels = mef.get_pixel_list(ip)
        for pix in exp_pixels:
            if pix in lin_curves: # one pixel shoudl be checked only once
                raise RuntimeError('[ERRROR] trying to re-count efficiency of pixel %i' % ep)
            lin_curves[pix] = {}
            pixpdf = pdf[pdf['pixel'] == pix]
            
            means = pixpdf.groupby(scannedvar)[vartoavg].mean()
            stds  = pixpdf.groupby(scannedvar)[vartoavg].std()

            lin_curves[pix]['means'] = means
            lin_curves[pix]['stds'] = stds

    return lin_curves

def DAC_to_ps_delay(dac):
    """ convert a delay DAC value to ps """
    # reg 999 : fine delay : 97 ps
    # reg 1000 : coarse delay : 1562 ps
    # dac : [coarse 7:4][fine 3:0]

    coarse_del = (dac >> 4) & 0xF
    fine_del   = dac & 0xF
    n_ps = 97*fine_del + 1562*coarse_del
    return n_ps

def DAC_to_ps_width(dac):
    """ convert a width DAC value to ps """

    dacvalue = dac & 31 # select 5 LSB
    n_ps = (dacvalue+1)*781.25
    return n_ps

DAC_to_ps_delay_vec = np.vectorize(DAC_to_ps_delay)
DAC_to_ps_width_vec = np.vectorize(DAC_to_ps_width)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',  help='input folder', required=True)
    parser.add_argument('--module', help='this is a module - read two asics (default : 1 asic)', default=False, action='store_true')
    # parser.add_argument('--output-curve',  help='output name for curves',    default='linear_scan.pdf')
    parser.add_argument('--output-curve',  help='output name for curves',    default='linear_scan.png')
    parser.add_argument('--prefix-output', help='prefix this string followde by _ to all output names', default=None)
    parser.add_argument('--output-dir',    help='output directory (prepend this + / to all output names)', default=None)
    parser.add_argument('--xrange0',       help='user defined x range for scan curves ASIC 0 (pass xmin, xmax)', nargs=2, default=None, type=float)
    parser.add_argument('--xrange1',       help='user defined x range for scan curves ASIC 1 (pass xmin, xmax)', nargs=2, default=None, type=float)
    parser.add_argument('--plot-x-DAC',    help='plot on the x axis the DAC value instead of the ps delay', default=False, action='store_true')
    parser.add_argument('--doOnly',        help='list of things to restrict in analysis (done at the df level). Pass a list of colX, rowX, or pixel numbers', nargs='+', default=None)
    args = parser.parse_args()

    print(f'[INFO] reading {args.input}')

    infos = mef.parse_infos(args.input)
    print(f'[INFO] Deduced properties :')
    print(f'       - meas type       : {infos["measType"]}')
    if 'Q' in infos:
        print(f'       - Q (inj. charge) : {infos["Q"]}')
    print(f'       - N (num. trig)   : {infos["N"]}')


    if infos["measType"] == 'widthScan':
        scanpoints = list(range(0, 32))  ## increasing Vth -> reducing eff
        timing_fname = 'timing_data__width_{dac}_.csv'
        if not args.plot_x_DAC:
            xtitle = 'Width [ps]'
        else:
            xtitle = 'DAC width'
        ytitle = 'TOT'
        yvar = 'tot'
        to_ps = DAC_to_ps_width_vec


    if infos["measType"].startswith('delayScan'):
        scanpoints = list(range(110, 160))  ## increasing Vth -> reducing eff
        timing_fname = 'timing_data_delay_{dac}_.csv'
        if not args.plot_x_DAC:
            xtitle = 'Delay [ps]'
        else:
            xtitle = 'DAC delay'
        ytitle = 'TOA'
        yvar = 'toa'
        to_ps = DAC_to_ps_delay_vec

    df, folderdictscanpoints = mef.open_scan_series_auto(
        args.input,
        timing_fname,
        scanpoints
    )

    if args.doOnly:
        print('[INFO] Restricting to', args.doOnly)
        toplot = []
        for todo in args.doOnly:
            toplot += mef.get_pixel_list(todo)
        toplot = sorted(list(set(toplot))) # make unique, and sort
        print('[INFO] Will filter to the following pixels: ', toplot)
        df = df[df.pixel.isin(toplot)]

    import matplotlib
    import matplotlib.pyplot as plt
    if not args.module:
        fig_crv, axs_crv = plt.subplots()
        fig_crv_std, axs_crv_std = plt.subplots()
        # fig_map, axs_map = plt.subplots()
        axs_crv = [axs_crv,]
        axs_crv_std = [axs_crv_std,]
        # axs_map = [axs_map,]
        nasic = 1
        df_list = [df]
    else:
        fig_crv, axs_crv = plt.subplots(2,1)
        fig_crv_std, axs_crv_std = plt.subplots(2,1)
        # fig_map, axs_map = plt.subplots(1,2,figsize=(20, 10))
        nasic = 2
        df0 = df[df.asicnumber == 0]
        df1 = df[df.asicnumber == 1]
        df_list = [df0, df1]

    xranges = [args.xrange0, args.xrange1]

    for iasic in range(nasic):
        df = df_list[iasic]

        lc = make_avg_df(df, folderdictscanpoints, yvar)
        for pix in lc.keys():

            if lc[pix]['means'].shape[0] == 0:
                continue # skip pixles not analysed in case you do --doOnly

            if args.plot_x_DAC:
                xvalues = lc[pix]['means'].index
            else:
                xvalues_dac = np.asarray(lc[pix]['means'].index)
                xvalues = to_ps(xvalues_dac)

            # axs_crv[iasic].plot(lc[pix]['means'], '-o', ms=1, lw=0.35, label=str(pix))
            # axs_crv_std[iasic].plot(lc[pix]['stds'], '-o', ms=1, lw=0.35, label=str(pix))

            axs_crv[iasic].plot(xvalues, lc[pix]['means'], '-o', ms=1, lw=0.35, label=str(pix))
            axs_crv_std[iasic].plot(xvalues, lc[pix]['stds'], '-o', ms=1, lw=0.35, label=str(pix))
        
        axs_crv[iasic].set_title(f'ASIC {iasic}')
        axs_crv[iasic].set_xlabel(xtitle)
        axs_crv[iasic].set_ylabel(ytitle + ' (mean)')

        axs_crv_std[iasic].set_title(f'ASIC {iasic}')
        axs_crv_std[iasic].set_xlabel(xtitle)
        axs_crv_std[iasic].set_ylabel(ytitle+ ' (std)')

        if xranges[iasic]:
            axs_crv[iasic].set_xlim(xranges[iasic][0], xranges[iasic][1])
            axs_crv_std[iasic].set_xlim(xranges[iasic][0], xranges[iasic][1])

    pref_string = infos['measType'] + '_'
    if args.prefix_output :
        pref_string  = pref_string + args.prefix_output + '_'
    if args.output_dir:
        pref_string = args.output_dir + '/' + pref_string

    fig_crv.tight_layout()
    fig_crv.savefig(pref_string + args.output_curve)

    fig_crv_std.tight_layout()
    fig_crv_std.savefig(pref_string + '_std_' + args.output_curve)
