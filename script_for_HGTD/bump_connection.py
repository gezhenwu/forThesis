import numpy as np
import pandas as pd
import argparse
import glob
import re
import matplotlib.pyplot as plt
from matplotlib import colors

def extract_infos(fbasename, pattern, prop_list):
    match_pattern = pattern.format(**{x : '(.*)' for x in prop_list})
    # print(match_pattern)
    p = re.compile(match_pattern)
    result = p.search(fbasename)
    # return result
    infos = {}
    for ip, p in enumerate(prop_list):
        infos[p] = result.group(ip+1)
    return infos


def make_ratio_plot(df_on, df_off, comptype, ytitle, title=None, connection_threshold=None, upper_threshold=None, yrcustomname=None, customlabels=None, mask=None):
    fig, axs = plt.subplots(2,2, gridspec_kw={'height_ratios': [3, 1]}, sharex='row', figsize=(10, 5))
    plt.ion()

    label0 = 'HV On'
    label1 = 'HV Off'
    if customlabels is not None:
        label0 = customlabels[0]
        label1 = customlabels[1]

    for iasic in [0,1]:
        p_df_on  = df_on.loc[iasic].reset_index()  # locate by asic row idx, then turn pixel asic back to a column again
        p_df_off = df_off.loc[iasic].reset_index() # locate by asic row idx, then turn pixel asic back to a column again
        axs[0, iasic].plot(p_df_on.pixel, p_df_on.threshold,   '-o', ms = 2, lw=0.5, c='red', label=label0)
        axs[0, iasic].plot(p_df_off.pixel, p_df_off.threshold, '-o', ms = 2, lw=0.5, c='blue', label=label1)
        # axs[iasic].set_ylim([ymin - 0.05*dy, ymax + 0.05*dy])
        axs[0, iasic].set_ylabel(ytitle)
        axs[0, iasic].legend(loc='best')
        # if args.yname:
            # axs[0].set_ylabel(args.yname)

        if comptype == 'diff':
            comp = p_df_on.threshold - p_df_off.threshold
            comp_dummy = p_df_off.threshold - p_df_off.threshold
            yrname = 'Diff. (on-off)'
            ylims = (-5, 10)
        elif comptype == 'ratio':    
            comp = p_df_on.threshold / p_df_off.threshold
            comp_dummy = p_df_on.threshold / p_df_on.threshold
            yrname = 'Ratio (on/off)'
            ylims = (0.9, 1.4)
        elif comptype == 'reldiff':    
            comp = (p_df_on.threshold - p_df_off.threshold )/ p_df_off.threshold
            comp_dummy = (p_df_off.threshold - p_df_off.threshold) / p_df_off.threshold
            yrname = 'Rel. diff. (on-off)/off'
            ylims = (-0.05, 0.3)
        else:
            raise RuntimeError('comp type not valid: %s' % args.comp)

        if yrcustomname is not None:
            yrname = yrcustomname

        axs[1, iasic].plot(p_df_on.pixel, comp_dummy, '-', ms = 2, lw=0.5, c='red')
        axs[1, iasic].plot(p_df_on.pixel, comp, '-o', ms = 2, lw=0.5, c='blue')
        # axs[1, iasic].set_ylim(ylims)
        axs[1, iasic].set_ylabel(yrname)

        # plot dashed lines for each column
        bds = list(range(16))
        bds = [15*x for x in bds]
        l0 = axs[0, iasic].get_ylim()
        l1 = axs[1, iasic].get_ylim()
        
        # lx = axs[0, iasic].get_xlim()
        lx = (0, 225)

        for b in bds:
            # print(l0, (b,b))
            # print(l1, (b,b))
            axs[0, iasic].plot((b,b), l0, '--', c='gray', lw = 0.5)
            axs[1, iasic].plot((b,b), l1, '--', c='gray', lw = 0.5)

            axs[1, iasic].plot((b,b), l1, '--', c='gray', lw = 0.5)

        if connection_threshold:
            ct = connection_threshold
            axs[1, iasic].plot(lx, (ct,ct), '--', c='black', lw = 0.5)

        if upper_threshold:
            cu = upper_threshold
            axs[1, iasic].plot(lx, (cu,cu), '--', c='black', lw = 0.5)

    if title is not None:
        fig.suptitle(title, fontsize=16)

    fig.tight_layout()    
    
    return fig, axs

def make_2D_map(df_on, df_off, comptype, ytitle, title=None, connection_threshold=None, upper_threshold=None):
    fig_map, axs_map = plt.subplots(1,2,figsize=(20, 10))
    for iasic in [0,1]:
        p_df_on  = df_on.loc[iasic].reset_index()  # locate by asic row idx, then turn pixel asic back to a column again
        p_df_off = df_off.loc[iasic].reset_index() # locate by asic row idx, then turn pixel asic back to a column again

        dfcomp = p_df_on.copy()

        if comptype == 'diff':
            dfcomp.threshold = p_df_on.threshold.sub(p_df_off.threshold)
            # comp_dummy = p_df_off.threshold - p_df_off.threshold
            yrname = 'Diff. (on-off)'
            # ylims = (-5, 10)
        elif comptype == 'ratio':    
            dfcomp.threshold = p_df_on.threshold.div(p_df_off.threshold)
            # comp_dummy = p_df_on.threshold / p_df_on.threshold
            yrname = 'Ratio (on/off)'
            # ylims = (0.9, 1.4)
        elif comptype == 'reldiff':    
            dfcomp.threshold = p_df_on.threshold.sub(p_df_off.threshold).div(p_df_off.threshold)
            # comp_dummy = (p_df_off.threshold - p_df_off.threshold) / p_df_off.threshold
            yrname = 'Rel. diff. (on-off)/off'
            # ylims = (-0.05, 0.3)
        else:
            raise RuntimeError('comp type not valid: %s' % args.comp)

        dfcomp['col'] = dfcomp.pixel // 15
        dfcomp['row'] = dfcomp.pixel % 15

        # dfcomp = fill_nondef_with(dfcomp, np.nan)
        # thrdata = np.asarray(list(thr[iasic].values()))
        # thrdata = np.reshape(thrdata, (15,15))
        # thrdata = thrdata.T
        # axs_map[iasic].imshow(thrdata, alpha=0.8, cmap='rainbow', origin='lower')
        grid = dfcomp.pivot(index='row', columns='col', values='threshold')
        
        # just plot connectivity value map
        if not connection_threshold:
            axs_map[iasic].imshow(grid, alpha=0.8, cmap='rainbow', origin='lower')

        # make a map with good/bad values
        else:
            # make a color map of fixed colors
            if not upper_threshold:
                cmap = colors.ListedColormap(['red', 'green'])
                bounds=[-999,connection_threshold,999]
                norm = colors.BoundaryNorm(bounds, cmap.N)
                axs_map[iasic].imshow(grid, alpha=0.8, cmap=cmap, origin='lower', norm=norm)
            else:
                cmap = colors.ListedColormap(['red', 'green', 'cyan'])
                bounds=[-999,connection_threshold,upper_threshold,999999]
                norm = colors.BoundaryNorm(bounds, cmap.N)
                axs_map[iasic].imshow(grid, alpha=0.8, cmap=cmap, origin='lower', norm=norm)

        # Loop over data dimensions and create text annotations.
        for i in range(15):
            for j in range(15):
                text = axs_map[iasic].text(j, i, grid.loc[i, j],
                               ha="center", va="center", color="black")

        Nd = 'n/a'
        if connection_threshold:
            Nd = 0
            for i in range(15):
                for j in range(15):
                    if grid.loc[i, j] < connection_threshold:
                        Nd += 1

        Nbad = None
        if upper_threshold:
            Nbad = 0
            for i in range(15):
                for j in range(15):
                    if grid.loc[i, j] >= upper_threshold:
                        Nbad += 1

        title = f'ASIC {iasic} - {Nd} disconnected'.format(iasic=iasic, Nd=Nd)
        if Nbad:
            title += ' and {} bad'.format(Nbad)
        axs_map[iasic].set_title(title)
        axs_map[iasic].set_xlabel('Column')
        axs_map[iasic].set_ylabel('Row')
        # axs_map[iasic].set_xticks(list(range(0, 15, 2)))
        # axs_map[iasic].set_yticks(list(range(0, 15, 2)))
        axs_map[iasic].set_xticks(list(range(0, 15, 1)))
        axs_map[iasic].set_yticks(list(range(0, 15, 1)))

    return fig_map, axs_map

# def make_lookup_dict(files_list, pattern, prop_list):
#     d = {}
#     for f in files_list:
#         infos = extract_infos(f, pattern, prop_list)
#         cd = d
#         for ip, p in enumerate(prop_list):
#             print(p)
#             if not p in cd:
#                 t = infos[p]
#                 print('..', t)
#                 cd[t] = {}
#                 cd = cd[t]
#         cd[prop_list[-1]] = f
#         cd = d
#     return infos

parser = argparse.ArgumentParser()
parser.add_argument('--input-folder', help='input folder with .csv threshold output files (for auto deduction of names)')
parser.add_argument('--title', help='Plot title', default=None)
parser.add_argument('--oname', help='output name', default='bump_connection_plot.pdf')
parser.add_argument('--oname-map', help='output name for 2D map', default='bump_connection_map.pdf')
parser.add_argument('--output-dir',    help='output directory (prepend this + / to all output names)', default=None)
parser.add_argument('--prefix-output', help='prefix this string followde by _ to all output names', default=None)
parser.add_argument('--comp',  help='type of ratio panel (diff, ratio, reldiff)', default='diff')
parser.add_argument('--meas',  help='type of measurement (4points, highQ, lowQ, QdiffHvOff, QdiffHvOn)', default='highQ')
parser.add_argument('--conn-thresh',  help='threshold to define connectivity (relative to the chosen comp)', default=None, type=float)
parser.add_argument('--upper-thresh',  help='upper threshold to define bad pixels (not used by default)', default=None, type=float)
parser.add_argument('--yratio-min',  help='min range on the y axis', default=None, type=float)
parser.add_argument('--yratio-max',  help='max range on the y axis', default=None, type=float)
parser.add_argument('--m-input-files', help='manually pass two csv files (code will make file[1] - file[0]', default=None, nargs='+')
parser.add_argument('--m-input-label', help='manually pass labels for the case above', default=None, nargs='+')
parser.add_argument('--mask', help='mask these pixels', default=None, nargs='+', type=int)
args = parser.parse_args()

print('[INFO] : looking for inputs in', args.input_folder)

if not args.m_input_files:

    keywords = ['HVstatus', 'Q']
<<<<<<< HEAD
    hvopts = ['On', 'Off']
    # qlist  = ['12', '24' '36']
    qlist = ['36']
=======
    # hvopts = ['On', 'Off']
    hvopts = ['Off']
    # qlist  = ['12', '24' '36']
    qlist = ['12','24']
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2

    proto_fname = 'thresScan_HV_{HVstatus}_Q_{Q}_threshold_list.csv'
    proto = args.input_folder + '/' + proto_fname


    all_files = glob.glob(proto.format(HVstatus='*', Q='*'))
    print('[INFO] : found', len(all_files), 'files :')
    for f in all_files:
        print('       : ', f)

    # ld = make_lookup_dict(all_files, proto_fname, keywords)

    ld = {}
    for f in all_files:
        infos = extract_infos(f, proto_fname, keywords)
        print(infos)
        hv = infos['HVstatus']
        q  = infos['Q']
        if not hv in ld:
            ld[hv] = {}
        ld[hv][q] = f

    dfs = {}

    for hv in hvopts:
        if not hv in dfs:
            dfs[hv] = {}
        for q in qlist:            
            df = pd.read_csv(ld[hv][q])
            ## reset the index, for the subtraction
            df = df.set_index(['asic','pixel'])
            if args.mask:
                for ipix in args.mask:
                    for iasic in [0,1]:
                        df.loc[(iasic,ipix), 'threshold'] = np.nan
            dfs[hv][q] = df


    if args.meas == '4points':
        print('[INFO] Making a 4 point measurement')
        conn_thr = args.conn_thresh if args.conn_thresh else 2
        df_on_delta  = dfs['On'][qlist[1]].threshold.subtract(dfs['On'][qlist[0]].threshold, fill_value=np.nan)
        df_off_delta = dfs['Off'][qlist[1]].threshold.subtract(dfs['Off'][qlist[0]].threshold, fill_value=np.nan)
        fig, axs = make_ratio_plot(df_on_delta, df_off_delta, args.comp, 'Threshold [DAC]', args.title, conn_thr, args.upper_thresh)
        fig_map, axs_map = make_2D_map(df_on_delta, df_off_delta, args.comp, 'Threshold [DAC]', args.title, conn_thr, args.upper_thresh)

    elif args.meas == 'lowQ':
        print('[INFO] Making a low Q measurement')
        conn_thr = args.conn_thresh if args.conn_thresh else 1
        fig, axs = make_ratio_plot(dfs['On'][qlist[0]], dfs['Off'][qlist[0]], args.comp, 'Threshold [DAC]', args.title, conn_thr, args.upper_thresh)
        fig_map, axs_map = make_2D_map(dfs['On'][qlist[0]], dfs['Off'][qlist[0]], args.comp, 'Threshold [DAC]', args.title, conn_thr, args.upper_thresh)

    elif args.meas == 'highQ':
        print('[INFO] Making a high Q measurement')
        conn_thr = args.conn_thresh if args.conn_thresh else 4
        fig, axs = make_ratio_plot(dfs['On'][qlist[-1]], dfs['Off'][qlist[-1]], args.comp, 'Threshold [DAC]', args.title, conn_thr, args.upper_thresh)
        fig_map, axs_map = make_2D_map(dfs['On'][qlist[-1]], dfs['Off'][qlist[-1]], args.comp, 'Threshold [DAC]', args.title, conn_thr, args.upper_thresh)

    elif args.meas == 'QdiffHvOn':
        print('[INFO] Making a map of differences (Qhigh - Qlow) for HV ON')
        conn_thr = None
        fig, axs = make_ratio_plot(dfs['On'][qlist[-1]], dfs['On'][qlist[0]], args.comp, 'Threshold [DAC]', args.title, conn_thr, None, yrcustomname='Diff.', customlabels=['Q = {}'.format(qlist[-1]), 'Q = {}'.format(qlist[0])] )
        fig_map, axs_map = make_2D_map(dfs['On'][qlist[-1]], dfs['On'][qlist[0]], args.comp, 'Threshold [DAC]', args.title, conn_thr, None)

    elif args.meas == 'QdiffHvOff':
        print('[INFO] Making a map of differences (Qhigh - Qlow) for HV Off')
        conn_thr = None
        fig, axs = make_ratio_plot(dfs['Off'][qlist[-1]], dfs['Off'][qlist[0]], args.comp, 'Threshold [DAC]', args.title, conn_thr, None, yrcustomname='Diff.', customlabels=['Q = {}'.format(qlist[-1]), 'Q = {}'.format(qlist[0])] )
        fig_map, axs_map = make_2D_map(dfs['Off'][qlist[-1]], dfs['Off'][qlist[0]], args.comp, 'Threshold [DAC]', args.title, conn_thr, None)

else: # manual file reading
    print('[INFO] Reading files')
    print(args.m_input_files[0])
    print(args.m_input_files[1])
    df0 = pd.read_csv(args.m_input_files[0])
    df1 = pd.read_csv(args.m_input_files[1])
    df0 = df0.set_index(['asic','pixel'])
    df1 = df1.set_index(['asic','pixel'])
    if args.mask:
        for ipix in args.mask:
            for iasic in [0,1]:
                df0.loc[(iasic,ipix), 'threshold'] = np.nan
                df1.loc[(iasic,ipix), 'threshold'] = np.nan

    print('[INFO] Making a map of differences of File1 - File0')
    conn_thr = args.conn_thresh
    upper_thr = args.upper_thresh
    fig, axs = make_ratio_plot(df1, df0, args.comp, 'Threshold [DAC]', args.title, conn_thr, upper_thr, yrcustomname='Diff.', customlabels=['File 1', 'File 0'] if not args.m_input_label else [args.m_input_label[1], args.m_input_label[0]] )
    fig_map, axs_map = make_2D_map(df1, df0, args.comp, 'Threshold [DAC]', args.title, conn_thr, upper_thr)


if args.yratio_min or args.yratio_max:
    for iratio in range(2):
        ax = axs[1, iratio]
        clim = list(ax.get_ylim())
        if args.yratio_min:
            clim[0] = args.yratio_min
        if args.yratio_max:
            clim[1] = args.yratio_max
        ax.set_ylim(clim)

odir = '' if not args.output_dir else args.output_dir + '/'

prefix = '' if not args.prefix_output else args.prefix_output + '_'

oname = odir + prefix + args.oname
oname_map = odir + prefix + args.oname_map

print('[INFO] saving figure as', oname)
fig.savefig(oname)

print('[INFO] saving 2D map as', oname_map)
fig_map.savefig(oname_map)
