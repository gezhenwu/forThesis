import numpy as np


# Define the dimensions of the matrix
rows, cols = 15, 15

# Create an empty matrix filled with zeros
matrix = np.zeros((rows, cols))

# Populate the matrix with the desired values
for row_position in range(rows):
    for col_position in range(cols):
        res=(row_position) + (col_position * 15)
        print (col_position, row_position, res)
        matrix[row_position, col_position] = int(res)


allSquareFive=[]
# Loop over the starting row indices of each square
for start_row in range(0, 15, 5):
    # Loop over the starting column indices of each square
    for start_col in range(0, 15, 5):
        # Extract the current square
        squareFive = matrix[start_row:start_row+5, start_col:start_col+5].flatten()
        print(squareFive)
        allSquareFive.append(squareFive)

allSquareThree=[]
# Loop over the starting row indices of each square
for start_row in range(0, 15, 3):
    # Loop over the starting column indices of each square
    for start_col in range(0, 15, 3):
        # Extract the current square
        squareThree = matrix[start_row:start_row+3, start_col:start_col+3].flatten()
        print(squareThree)
        allSquareThree.append(squareThree)
        

allSparse=[]
for sparse_index in range(15):
    sparse = []
    # Loop over the elements in the current sparse
    for i in range(15):
        col=(sparse_index+i+7*(i%2))%15
        row=(sparse_index+i)%15
        value = matrix[col,row]
        sparse.append(value)
    print (sparse)
    allSparse.append(sparse)


print ( len(allSparse), len(allSquareThree), len(allSquareFive))


        
