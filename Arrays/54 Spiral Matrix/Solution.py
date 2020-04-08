class Solution:
    def spiralOrder(self, matrix):
        
        if not matrix:
            return []
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        size = len(matrix) * len(matrix[0])
        output = []
        while top<=bottom and left<=right:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left -1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
        return output