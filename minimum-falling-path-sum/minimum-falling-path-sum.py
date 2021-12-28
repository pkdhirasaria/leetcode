class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for __ in range(row)]
        for i in range(col):
            dp[0][i] = matrix[0][i]            
        for i in range(1,row):
            for j in range(col):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == col-1:
                    dp[i][j] =  matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:    
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1],dp[i-1][j-1])
        # print(dp)
        return min(dp[-1])