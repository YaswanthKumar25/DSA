class Solution:
    def rotateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for ind,value in enumerate(matrix):
            matrix[ind]=value[::-1]
        