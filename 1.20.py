import numpy as np
def SumMatrix1(matrix):
    total = 0 
    matrix.shape

    for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if j % 2 == 0:
                    total += matrix[i][j]
    return total

def SumMatrix2(matrix):
    total = 0 
    matrix.shape

    for i in range(matrix.shape[0]):
        if i % 2 == 0:
            for j in range(matrix.shape[1]):
                if j % 2 == 0:
                    total += matrix[i][j]
    return total

def VariationMatrix(matrix):
    return np.max(matrix, axis=1) - np.min(matrix, axis=1)

def main():

    np_matrix = np.array([
    [3, 5, 7, 2],
    [8, 6, 4, 9],
    [1, 2, 3, 4],
    [5, 7, 9, 0]
])

    print("Sum of even elements (Method 1):", SumMatrix1(np_matrix))
    print("Sum of even elements (Method 2):", SumMatrix2(np_matrix))
    print("Variation of each row:", VariationMatrix(np_matrix))

if __name__ == "__main__":
    main()