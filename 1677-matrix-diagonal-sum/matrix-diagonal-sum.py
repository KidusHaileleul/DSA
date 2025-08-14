class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        i = 0
        x = 0
        while i < n:
            x += mat[i][i]
            i += 1
        j = 0
        y = 0
        while j<n:
            y+=mat[j][n-1-j]
            j+=1
        if n % 2 == 1:
            return (x+y)-mat[n//2][n//2]
        else:
            return x+y
        