a = [[3,1,5],
     [2,4,6],
     [4,5,6]]

b = [[4,3,5],
     [8,9,1],
     [6,7,5]]


if len(a) != len(b) or len(a[0]) != len(b[0]):
    print("To perform addition Matrices size needs to be equal.")
else:
    result=[[0]*len(a[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
print(result)


# def add_matrices(matrix1, matrix2):
#     # Check if the matrices have the same dimensions
#     if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
#         return "Matrices must have the same dimensions to perform addition."
    
#     # Create an empty result matrix with the same dimensions as the input matrices
#     result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]
    
#     # Perform element-wise addition
#     for i in range(len(matrix1)):
#         for j in range(len(matrix1[0])):
#             result[i][j] = matrix1[i][j] + matrix2[i][j]
    
#     return result

# # Example matrices
# matrix1 = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]

# matrix2 = [[9, 8, 7],
#            [6, 5, 4],
#            [3, 2, 1]]

# # Add the matrices
# result_matrix = add_matrices(matrix1, matrix2)
# if isinstance(result_matrix, str):
#     print(result_matrix)
# else:
#     # Print the result matrix
#     for row in result_matrix:
#         print(row)
