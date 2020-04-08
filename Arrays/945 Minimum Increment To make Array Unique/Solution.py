class Solution:
    def minIncrementForUnique(self, A) -> int:
        
        A.sort()
        inc = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1]:
                inc += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        return inc