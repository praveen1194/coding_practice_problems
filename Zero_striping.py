from typing import List

# For each zero in an m x n matrix, set its entire row and column to zero in place
def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    
    # the method is to check all the number except the ones in the first row and first column. 
    # So starting from matrix[1][1] we traverse each row till the end
    # if we encounter a '0' we set the corresponding first value in its row (matrix[0][col index of 0 value]) and first value in its column (matrix[row index of 0 value][0]) as 0
    # Now we will have 0 indicators in the first rows and first column to indicate which rows and which columns need to have '0'
    rowCount = len(matrix)
    colCount = len(matrix[0])

    # Before we start the first traversal to check '0's, we need to record if there are any existing '0's in the first row or first column 
    # If there is, then we will need to update the values in First row or First column to '0' in the end after we have updated all the values in the rest of the matrix 
    # This is important becasue if there are no '0's in the matrix but only in the first row or first column then we will not make any changes in the matrix and get a wrong answer

    # If we update the First row and First column before updating the rest of the matrix,
    # then we will end up having all the references to '0' and will end up with the entire matrix with only '0' values which will also be wrong
    zeroInFirstRow = False      
    zeroInFirstCol = False
    
    # Checking if First row has a '0', if yes then we will update the entire first row to '0' in the end
    for j in range(colCount):                
        if matrix[0][j] == 0:
            zeroInFirstRow = True

    # Checking if First Column has a '0', if yes then we will update the entire first column to '0' in the end
    for i in range(rowCount):
        if matrix[i][0] == 0:
            zeroInFirstCol = True

    # First traversal to mark the corresponding values in the first row and first column to '0'
    for i in range(1, rowCount):
        for j in range(1, colCount):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    # Second traversal to update all the values (which have '0' in their first row or first column) to '0'
    for i in range(1, rowCount):
        for j in range(1, colCount):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Update the entire first row to '0' if the First row had zero
    if zeroInFirstRow:
        for j in range(colCount):
            matrix[0][j] = 0

    # Update the entire first column to '0' if the First column had zero
    if zeroInFirstCol:
        for i in range(rowCount):
            matrix[i][0] = 0

    return

matrix = [[1, 2, 3, 4, 5],
          [6, 0, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 0]]

zero_striping(matrix)

print(matrix)