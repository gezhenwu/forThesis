import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to group and plot the data
def group_and_plot(df):
    # Group the data by specified columns and calculate the mean of 'median'
    df=df[df["Cp"]==1]
    varList=['On', 'Inj', 'board', 'Ctest', 'Cd', 'Rtest', 'Cp']
    grouped_df = df.groupby(varList)['median'].mean().reset_index()
    group_map={}
    # Iterate over each group and plot the mean as a function of Cd as scatter points
    var2List=['On', 'Inj', 'board', 'Cp']
    for group_name, group_data in grouped_df.groupby(var2List):
        key= str([str(x) + ' ' + str(y) for x, y in zip(var2List,group_name)])
        group_map[key] = (group_data['Cd'], group_data['median'])
        plt.scatter(group_data['Cd'], group_data['median'], label=key)

    # Set labels and title for the plot
    plt.xlabel('Cd')
    plt.ylabel('DeltaVth [DACU]')
    #plt.title('Mean as a Function of Cd for different configurations')
    plt.legend()

    # Set the lower bound of the y-axis to 0
    plt.ylim(bottom=0)
    plt.ylim(top=100)
    return group_map

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Generate scatter plot of mean as a function of Cd')

# Add arguments for the filenames with shortcuts
parser.add_argument('-f1', '--filename1', type=str, help='First CSV file to read the data from')
parser.add_argument('-f2', '--filename2', type=str, help='Second CSV file to read the data from')

# Parse the command-line arguments
args = parser.parse_args()
filename1 = args.filename1
filename2 = args.filename2

# Read the CSV files into separate DataFrames
df1 = pd.read_csv(filename1)
df2 = pd.read_csv(filename2)

# Generate and save the first plot
plt.figure()
map1=group_and_plot(df1)
plt.savefig(filename1+"_cdSummary.png")

# Generate and save the second plot
plt.figure()
map2=group_and_plot(df2)
plt.savefig(filename2+"_cdSummary.png")


# Find and print common keys and their values in the two maps
common_keys = set(map1.keys()).intersection(map2.keys())
plt.figure()
for key in common_keys:
    if np.array_equal(map1[key][0],map2[key][0]):
        ratio = map2[key][1] / map1[key][1]*7.8/1.7*23/12.5
        print (np.array(map1[key][1]), np.array(map2[key][1]), np.array(ratio))
        plt.scatter(map1[key][0], ratio, label=key)
        plt.xlabel('Cd')
        #plt.ylabel('Large/Small Ctest')
plt.legend()
plt.savefig(filename1+"_cdSummaryRatio.png")
plt.close()


