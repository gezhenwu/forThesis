import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
import argparse
import os
import sys

matplotlib.rcParams["legend.fontsize"] = 15
matplotlib.rcParams["xtick.labelsize"] = 20
matplotlib.rcParams["ytick.labelsize"] = 20
matplotlib.rcParams["axes.titlesize"] = 20
matplotlib.rcParams["axes.labelsize"] = 20

color_list = [
    "red",
    "blue",
    "cyan",
    "darkgreen",
    "black",
    "gold",
    "magenta",
    "chocolate",
    "teal",
    "yellowgreen",
]


def openFiles(fname):
    ret = {}
    with open(fname) as fList:
        np_files = fList.readlines()
        for f in np_files:
            print(f.split(" "))
            label = f.split(" ")[0]
            np_Q = np.load(f.split(" ")[1].strip())
            npdata = np.load(f.split(" ")[2].strip())
            #npdata[npdata == 0] = npdata[0]
            ret[label] = (np_Q, npdata)
    return ret

def quadraticDiff(a,b):
    c=np.sqrt(np.power(a,2)-np.power(b,2))
    return c


def drawPlot(np_vector, figurename):
    plt.figure(figsize=(20, 10))

    # ax1.plot(x_axis, np_vector[basename], label=basename, linestyle='-', color=color_list[0], lw=1.5)
    i_color = 0
    for label, np_array_vec in np_vector.items():
        np_Q = np_array_vec[0]
        np_array = np_array_vec[1]
        # if label == basename:
        #    continue
        floor = 0
        if len(np_array[np_array > 0]) > 0:
            floor = np.min(np_array[np_array > 0])
        plt.plot(
            np_Q,
            quadraticDiff(np_array, floor),
            label=label,
            linestyle="-",
            color=color_list[i_color],
            lw=2,
        )
        i_color += 1
    plt.xlabel("Q [fC]")
    plt.ylabel("TOARMSmedian (subtracted)")
    # ax1.set_ylim(0, 3.5)
    plt.ylim(0, plt.ylim()[1] * 1.2)
    plt.xlim(left=2., right=20)
    plt.legend(loc="upper right", ncol=2)

    plt.savefig(figurename + ".png")
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--outputName")
    parser.add_argument("-y", "--yname")
    parser.add_argument("-b", "--basename")
    parser.add_argument("-d", "--draw2d")

    args = parser.parse_args()
    np_array = openFiles(args.input)
    drawPlot(np_array, args.outputName)
