import numpy as np
import glob
import matplotlib.pyplot as plt
import re

for pix in range (0,15):
    # Create a figure
    fig, ax = plt.subplots()

    # Define the file pattern
    file_pattern = 'Plots/ALTIROC3B_*_Vth_*_Ctest_26___eff_'+str(pix)+'.npz'
    
    # Get the list of files matching the pattern
    file_list = glob.glob(file_pattern)
    
    # Print the list of files
    for file in file_list:
        print(file)
        data = np.load(file)

        # Access the arrays using the names provided during saving
        Q = data['array1']
        eff = data['array2']

        # Extract the three digits after "Vth_"
        vth_digits = re.findall(r'Vth_(\d{3})', file)
        if vth_digits:
            vth_label = vth_digits[0]
        else:
            vth_label = 'Unknown'

        print (vth_label,Q,eff)

        # Check if all elements in eff are equal to 1
        if np.all(eff == 1):
            continue  # Skip plotting if all elements are equal to 1

        # Check if all elements in eff are equal to 0
        if np.all(eff == 0):
            continue  # Skip plotting if all elements are equal to 1

        # Plot the eff vs Q for the current file
        plt.plot(Q, eff, label=f'{vth_label}')  # Add a label with the file name

    # Add labels and a legend to the plot
    plt.xlabel('Charge (fC)')
    plt.ylabel('Efficiency')
    plt.legend()
    
    # Show the plot
    plt.savefig("Plots/single_"+str(pix)+".png")

# # Print the loaded arrays
# print("Loaded Array 1:", loaded_array1)
# print("Loaded Array 2:", loaded_array2)
