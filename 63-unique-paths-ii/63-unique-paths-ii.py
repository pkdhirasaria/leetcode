class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        row,col = len(mat),len(mat[0])
        dp = [[0 for _ in range(col)] for __ in range(row)]
        print(dp)
        if mat[0][0] !=1:
            dp[0][0] = 1
        for i in range(1,col):
            if mat[0][i] == 1:
                break
            dp[0][i] = dp[0][i-1]
        for i in range(1,row):
            if mat[i][0] == 1:
                break
            dp[i][0] = dp[i-1][0]
        for i in range(1,row):
            for j in range(1,col):
                if mat[i][j] != 1:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[row-1][col-1]
       