"""
CS361 - HW2
Problem 6 - Sort Matrix Diagonals
Author @Shrey Poshiya
"""

def sortMatrixDiagonals(matrix):

    # only need to do sorting starting from the first elements from the first n-1 rows and m-1 columns

    numRows = len(matrix)
    numCols = len(matrix[0])

    # column logic:
    # iterate through the first n-1 columns
    for col in range(numCols - 1):
        
        # intiailzie iteration variables
        iterRow = 0
        iterCol = col
        diagonal = []
        # get the diagonal elements (iterates through the diagonal)
        while iterRow < numRows and iterCol < numCols:
            diagonal.append(matrix[iterRow][iterCol])
            iterRow += 1
            iterCol += 1
        
        # sort the diagonal list
        insertionSort(diagonal)

        # replace the diagonal elements in the matrix
        # reset iteration variables
        iterRow = 0
        iterCol = col
        for val in diagonal:
            matrix[iterRow][iterCol] = val
            iterRow += 1
            iterCol += 1
            
    # row logic:
    # iterate through the first m-1 rows
    # skip over row 0 since that was done in column log
    for row in range(1, numRows - 1):
        iterRow = row
        iterCol = 0
        diagonal = []
        # get the diagonal elements (iterates through the diagonal)
        while iterRow < numRows and iterCol < numCols:
            diagonal.append(matrix[iterRow][iterCol])
            iterRow += 1
            iterCol += 1

        # sort the diagonal list
        insertionSort(diagonal)

        # replace the diagonal elements in the matrix
        # reset iteration variables
        iterRow = row
        iterCol = 0
        for val in diagonal:
            matrix[iterRow][iterCol] = val
            iterRow += 1
            iterCol += 1

# using insertion sort algo that I wrote from problem 2
def insertionSort(A):
   
    assert len(A) > 0, "error, ensure that provided list is NOT empty"

    for i in range(1, len(A)):
        # initialzie 
        key = A[i]
        j = i - 1
        # shift up any elements that are greater than the key
        while j >= 0 and key <= A[j]:
            A[j + 1] = A[j]
            j  -= 1
        # move the key behind the shited up elements
        A[j+1] = key
    return A

def main():
    matrix = [[3,3,1,1],
              [2,2,1,2],
              [1,1,1,2]]
    
    print(f"Original matrix:")
    for row in matrix:
        print(row)

    sortMatrixDiagonals(matrix)

    print(f"Sorted matrix:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()