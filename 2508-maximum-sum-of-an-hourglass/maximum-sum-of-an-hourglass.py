class Solution:
    def maxSum(self, x: List[List[int]]) -> int:
        return max(
            x[i][j] + x[i][j+1] + x[i][j+2] +
            x[i+1][j+1] +
            x[i+2][j] + x[i+2][j+1] + x[i+2][j+2]
            for i in range(len(x)-2)
            for j in range(len(x[0])-2))


        