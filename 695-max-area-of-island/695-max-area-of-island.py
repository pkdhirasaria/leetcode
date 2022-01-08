class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        # vis = set()
        def dfs(i,j):
            if i >= row or j >= col or i < 0 or j < 0 or grid[i][j] == 0:
                return 0
            # self.c += 1            
            grid[i][j] = 0
            l = dfs(i+1,j)
            r = dfs(i,j+1)
            u = dfs(i-1,j)
            d = dfs(i,j-1)
            return l + r+u+d + 1
        
        count= 0    
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # self.c = 0
                    d = dfs(i,j)
                    # print(i,j,d)
                    count = max(d,count)
        return count