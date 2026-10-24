class Solution:
    def spiralOrder(self, matrix):
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        ans = []

        while left <= right and top <= bottom:

            i = left
            while i <= right:
                ans.append(matrix[top][i])
                i += 1
            top += 1

            i = top
            while i <= bottom:
                ans.append(matrix[i][right])
                i += 1
            right -= 1

            if top <= bottom:          
                i = right
                while i >= left:
                    ans.append(matrix[bottom][i])
                    i -= 1
                bottom -= 1

            if left <= right:          
                i = bottom
                while i >= top:
                    ans.append(matrix[i][left])
                    i -= 1
                left += 1

        return ans