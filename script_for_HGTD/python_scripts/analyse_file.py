# python  analyse_file.py --input ../../../../../FastFadaMeasurements/Measurements2ASIC/Qmin_fullmodule_12Apr2024_Nathalie_vthcToMax/chargeScan/B_None_On_col_Inj_col_N_100_Vth_380_Q_81/pixelOn_col*_pixelInj_col*/timing_data_dacCharge_127.csv

import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
import makeEffCurve as mef
matplotlib.use('Agg')

def df_from_list(dflist, parse_infos=True):
    dfs = []
    for f in dflist:
        d = pd.read_csv(f)
        if parse_infos:
            p = os.path.normpath(f)
            infos = mef.parse_infos('/'.join(p.split('/')[:-1]))
            for ii in infos:
                d[ii] = infos[ii]
        dfs.append(d)
    df = pd.concat(dfs)
    return df

def restrictToInjectedPixels(df):
    df['injList'] = df['pixelInj'].apply(mef.get_pixel_list)
    df['wasInjected'] = df.apply(lambda row : row['pixel'] in row['injList'], axis=1)
    df = df[df['wasInjected']]
    return df

def add_col_row_info(df):
    df['col'] = df['pixel'] // 15
    df['row'] = df['pixel'] % 15
    return df

def pix_to_col_row(pix):
    """ return (col, row) pair """
    return (pix//15, pix%15)

def fill_missing_with_nan(map_df):
    """ returns a new df that contains one new row filled with nans for missing pixels """
    expected_values = pd.DataFrame({'pixel': range(225)})
    expected_values = add_col_row_info(expected_values)
    df_merged = pd.merge(expected_values, map_df, on=['pixel', 'col', 'row'], how='left')
    return df_merged

def make_2D_map(fig, ax, df, column, annotate=True, annot_format='{:.0f}'):
    """ make a 2D plot of the contect of df organized in a 15x15 matrix """
    if 'col' not in df.keys() or 'row' not in df.keys():
        df = add_col_row_info(df)
    
    matrix = df.pivot(index='row', columns='col', values=column)

    im = ax.imshow(matrix, alpha=0.8, cmap='rainbow', origin='lower')
    # Loop over data dimensions and create text annotations.
    for col in range(15):
        for row in range(15):
            text = ax.text(row, col, annot_format.format(matrix.values[col, row]),
                           ha="center", va="center", color="black", fontsize='small')
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.set_xticks(list(range(0, 15, 1)))
    ax.set_yticks(list(range(0, 15, 1)))

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im, cax=cax)    

def aggregate_and_make_2D_map(fig, ax, df, column, aggr_function=np.mean, annotate=True, annot_format='{:.0f}', fillnan_with=None):
    """ make a 2D map from df for all values of column divided by pixel.
        Aggregate multiple values into a single number using aggr_function """

    gr  = df.groupby('pixel')

    col = []
    row = []
    pix = []
    val = []

    for p, item in gr:
        # print(gr.get_group(pix), "\n\n")
        c, r = pix_to_col_row(p)
        v = aggr_function(item[column])
        col.append(c)
        row.append(r)
        pix.append(p)
        val.append(v)

    map_df = pd.DataFrame({'col' : col, 'row' : row, 'pixel' : pix, 'val' : val})
    map_df = fill_missing_with_nan(map_df)
    if fillnan_with is not None:
        map_df = map_df.fillna(fillnan_with)
    make_2D_map(fig, ax, map_df, 'val', annotate, annot_format)
    # matrix = map_df.pivot(index='row', columns='col', values='val')

    # im = ax.imshow(matrix, alpha=0.8, cmap='rainbow', origin='lower')
    # # Loop over data dimensions and create text annotations.
    # for col in range(15):
    #     for row in range(15):
    #         text = ax.text(row, col, annot_format.format(matrix.values[col, row]),
    #                        ha="center", va="center", color="black", fontsize='small')
    # ax.set_xlabel('Column')
    # ax.set_ylabel('Row')
    # ax.set_xticks(list(range(0, 15, 1)))
    # ax.set_yticks(list(range(0, 15, 1)))

    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("right", size="5%", pad=0.05)
    # plt.colorbar(im, cax=cax)
    # # fig.colorbar(im, ax)
    # # print(matrix.values)
    # # ax.colorbar()        


parser = argparse.ArgumentParser()
parser.add_argument('--input',  help='csv file to analyse', required=True, nargs='+')
parser.add_argument('--asics',  help='ASICs numbers to analyse', default=[0,1], type=int, nargs='+')
parser.add_argument('--output', help='output folder', default='plots/')
parser.add_argument('--restrictToInjected', help='filter dataframe to keep only pixels where injection was done', default=False, action='store_true')

args = parser.parse_args()

# print('... analysing file', args.input)
print(f'... analysing {len(args.input)} files')
print(f'... will make plots for {len(args.asics)} asics : ', args.asics)
print(f'... will save plots in {args.output}')

asic_i2c_map = {i : i+2 for i in args.asics} # map asic nr to i2c address

df = df_from_list(args.input)
print('... read file with', df.shape[0], 'entries')

if args.restrictToInjected:
    print('... filtering dataframe to keep only pixels where injection was done')
    df = restrictToInjectedPixels(df)
    
ops_list = {
    'toa'   : ['mean', 'std'],
    'tot'   : ['mean', 'std'],
    'pixel' : ['count'],
}

ops_def = {
    'mean'  : np.mean,
    'std'   : np.std,
    'count' : np.size
}

ops_kwargs = {
    'mean'  : {},
    'std'   : {},
    'count' : {'fillnan_with' : 0},
}

ops_name = {
    'mean'  : 'Mean',
    'std'   : 'Std dev.',
    'count' : "Occupancy",
}

prop_name = {
    'tot'   : 'TOT',
    'toa'   : 'TOA',
    'pixel' : 'Pixel',
}

# prepare out fodler
if not os.path.isdir(args.output):
    os.makedirs(args.output)

# pixel : use to make occunacy plots
for prop in ['toa', 'tot', 'pixel']:
    print('... plotting', prop)
    for op in ops_list[prop]:
        print('... ... doing', op)
        # NOTE : might need optimization for > 2 asic
        fig, axs = plt.subplots(1, len(args.asics), figsize=(20, 10))

        if len(args.asics) == 1:
            axs = [axs,]

        kwa = ops_kwargs[op]
        for it, iasic in enumerate(args.asics):
            i2caddr = asic_i2c_map[iasic]
            pdf = df[df.asic == i2caddr]
            aggregate_and_make_2D_map(fig, axs[it], pdf, prop, ops_def[op], **kwa)

        fig.suptitle(f'{prop_name[prop]} {ops_name[op]}')
        oname = os.path.join(args.output, f'{prop}_{op}.pdf')

        fig.savefig(oname)