class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        empty = 2147483647
        gate = 0
        row, col = len(rooms), len(rooms[0])
        vis = set()
        isValid = lambda x, y: 0 <= x < row and 0 <= y < col and rooms[x][y] == empty
        path = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == gate:
                    q.append((i, j, 0))
                    vis.add((i, j))
        while q:
            x, y, level = q.popleft()
            for dx, dy in path:
                x1= x + dx
                y1 = y + dy
                if isValid(x1, y1):
                    rooms[x1][y1] = rooms[x][y] + 1
                    q.append((x1, y1, level + 1))
                    vis.add((x1, y1))