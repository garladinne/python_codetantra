matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#for row in matrix : 
print("Matrix before transposition:",matrix)
print("Length of the matrix is:",len(matrix))
rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
#print("\n") 
#for row in rez: 
print("Matrix after transposition:",rez) 
# find the transpose of the matrix and print the result as shown in the example above
