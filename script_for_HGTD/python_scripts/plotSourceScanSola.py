import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import os
# from pathlib import Path
import time

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

def list_files(base_folder, verbose=False):
    all_flist = []
    all_folders = [f.path for f in os.scandir(base_folder) if f.is_dir()]
    if verbose: print (f'[INFO] : identified {len(all_folders)} subfolders to analyse')
    for fol in all_folders:
        basename = os.path.basename(os.path.normpath(fol))
        if verbose: print (' - : ', basename)
        infos = parse_infos(fol)
        flist = os.listdir(fol)
        flist.sort(key = lambda x : int(x.split('_')[-2])) # to sort properly in numerical order
        if verbose:
            print('... folder has', len(flist), 'files:')
            for f in flist:
                print('      .. ', f)
        for f in flist:
            fname = '/'.join([fol, f])
            all_flist.append(fname)
    return all_flist

def open_file_list(flist, verbose=False):
    dflist = []
    for f in flist:
        pdf = open_file(f)
        dflist.append(pdf)
    df = pd.concat(dflist)
    return df

def open_file_series(base_folder):
    """ this loops on all folders inside the base_folder """
    dflist = []
    pointsfound = {}
    all_folders = [f.path for f in os.scandir(base_folder) if f.is_dir()]
    print (f'[INFO] : identified {len(all_folders)} subfolders to analyse')
    for fol in all_folders:
        basename = os.path.basename(os.path.normpath(fol))
        print (' - : ', basename)
        infos = parse_infos(fol)
        flist = os.listdir(fol)
        flist.sort(key = lambda x : int(x.split('_')[-2])) # to sort properly in numerical order
        print('... folder has', len(flist), 'files:')
        for f in flist:
            print('      .. ', f)        
        for f in flist:
            nstep = int(f.split('_')[-2])
            pdf = open_file('/'.join([fol, f]), newColName='iteration', newColVal=nstep) # this is OK only if a sinle subfolder is found
            dflist.append(pdf)
    df = pd.concat(dflist)
    return df

def check_and_update(base_folder):
    print('[INFO] : starting to scan', base_folder, ' - interrupt with ctrl-C')
    matplotlib.use('QtAgg')
    old_flist = []
    poll_time = 10 # in seconds
    fig, axs = plt.subplots(1,2,figsize=(20, 10))
    plt.ion()

    while True:
        flist = list_files(base_folder, verbose=False)
        new_files = [x for x in flist if x not in old_flist]
        if len(new_files) == 0 or len(flist) == 0:
            time.sleep(poll_time)
        else:
            time.sleep(0.5)
            print('...', len(new_files), 'new files found, updating')
            old_flist = list(flist)
            df = open_file_list(flist, verbose=False)
            make_2D_map(df, title=None, fig=fig, axs=axs)
            plt.show()


def col_row_to_ipix(col, row):
    return 15*col + row

def ipix_to_col_row(ipix):
    return (ipix//15, ipix%15)

###############################################################

def make_2D_map(df, title=None, fig=None, axs=None, mask0=None, mask1=None):
    if fig is None or axs is None:
        fig_map, axs_map = plt.subplots(1,2,figsize=(20, 10))
    else:
        fig_map = fig
        axs_map = axs

    if mask0 is None:
        mask0 = []
    if mask1 is None:
        mask1 = []

    masks = [mask0, mask1]

    df['col'] = df.pixel // 15
    df['row'] = df.pixel % 15
    
    cmap_name = 'viridis' # color map name
    zero_color = 'white' # color of the empty pixels (counts = 0)

    for iasic in [0,1]:
        # p_df  = df.loc[iasic].reset_index()  # locate by asic row idx, then turn pixel asic back to a column again
        p_df = df[df.asicnumber == iasic]
        if p_df.shape[0] == 0:
            continue
        cmap = matplotlib.cm.get_cmap(cmap_name)
        # cmap.set_bad(color='blue')
        cmap.set_under(color=zero_color)

        bins = np.linspace(0-0.5, 15-0.5, 16)
        histdata, _, _, _ = axs_map[iasic].hist2d(p_df['col'], p_df['row'], bins=bins, cmap=cmap, vmin=0.5)
        print(histdata)

        axs_map[iasic].set_title(f'ASIC {iasic}')
        axs_map[iasic].set_xlabel('Column')
        axs_map[iasic].set_ylabel('Row')
        # axs_map[iasic].set_xticks(list(range(0, 15, 2)))
        # axs_map[iasic].set_yticks(list(range(0, 15, 2)))
        axs_map[iasic].set_xticks(list(range(0, 15, 1)))
        axs_map[iasic].set_yticks(list(range(0, 15, 1)))

        for i in range(15):
            for j in range(15):
                ipix = col_row_to_ipix(j, i)
                if ipix in masks[iasic]:
                    continue
                text = axs_map[iasic].text(j, i, histdata[j, i],
                               ha="center", va="center", color="black")

        # plot masks
        rsize = 1
        offs = 0.5
        for mpix in masks[iasic]:
            col, row = ipix_to_col_row(mpix)
            print(col,row)
            rect = matplotlib.patches.Rectangle((col-offs,row-offs), rsize, rsize, fill=None, hatch='///', color='red')
            axs_map[iasic].add_patch(rect)

    if title: fig_map.suptitle(title)
    return fig_map, axs_map

def print_summary(df):
    df0 = df[df.asicnumber == 0]
    df1 = df[df.asicnumber == 1]

    pixs_0 = sorted(list(df0.pixel.unique()))
    pixs_1 = sorted(list(df1.pixel.unique()))

    print("=============================================")
    print("The following pixels have > 0 counts (ASIC 0 : {}, ASIC 1 : {})".format(len(pixs_0), len(pixs_1)))
    print("=============================================")
    print('--- ASIC 0 :')
    print(','.join([str(i) for i in pixs_0]))
    print('\n')
    print('--- ASIC 1 :')
    print(','.join([str(i) for i in pixs_1]))

    allpix = list(range(225))
    miss_0 = [p for p in allpix if p not in pixs_0]
    miss_1 = [p for p in allpix if p not in pixs_1]
    print('\n\n')
    print("=============================================")
    print("The following pixels have 0 counts (ASIC 0 : {}, ASIC 1 : {})".format(len(miss_0), len(miss_1)))
    print("=============================================")
    print('--- ASIC 0 :')
    print(','.join([str(i) for i in miss_0]))
    print('\n')
    print('--- ASIC 1 :')
    print(','.join([str(i) for i in miss_1]))

###############################################################

parser = argparse.ArgumentParser()
parser.add_argument('--input',        help='input folder', required=True)
parser.add_argument('--live',         help='live updating plot', action='store_true', default=False)
parser.add_argument('--mask0',        help='List of masked pixels for ASIC 0', type=int, default=[], nargs='+')
parser.add_argument('--mask1',        help='List of masked pixels for ASIC 1', type=int, default=[], nargs='+')
parser.add_argument('--output-dir',   help='output directory', default='')
parser.add_argument('--title',        help='plot title', default='')
parser.add_argument('--tag',          help='tag of this measurement (for output file name)', default=None)

args = parser.parse_args()


if not args.live:
    df = open_file_series(args.input)

    fig_map, axs_map = make_2D_map(df, title=args.title, mask0=args.mask0, mask1=args.mask1)


    fig_map.tight_layout()
    odir = '' if not args.output_dir else (args.output_dir + '/')
    oname =  odir + 'sourcescan' + (f'_{args.tag}' if args.tag else '') + '.pdf'
    print('... saving plot as', oname)
    fig_map.savefig(oname)

    print_summary(df)

else:
    check_and_update(args.input)

