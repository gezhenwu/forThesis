import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = 'Data3/B_9_2023_07_17_setup1_largerN/chargeScan/B_9_On_all_Inj_pix_N_10000_Vth_395_cDel_0_fDel_9_Ctest_26_/pixelOn_all_pixelInj_1/timing_data_dacCharge_127_.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Extract the 'toa' column
toa_values = df['toa']

# Calculate the Root Mean Square (RMS) of 'toa' values using numpy
rms = np.std(toa_values )

# Create a list of row numbers (0-based index) to use as x-axis for plotting
row_numbers = range(len(toa_values))

# Set the figure size to have width 4 times larger than height
fig_width = 12  # 12 inches for width (4 times larger than height)
fig_height = fig_width / 4  # Calculate height based on the desired ratio
plt.figure(figsize=(fig_width, fig_height))

# Plot 'toa' as a function of row number
plt.scatter(row_numbers, toa_values)#, marker='o')#, linestyle='-')
plt.xlabel('Row Number')
plt.ylabel('toa')
plt.title(f'RMS: {rms:.2f} LSB')
plt.grid(True)


plt.savefig("Plots/toto.png")
