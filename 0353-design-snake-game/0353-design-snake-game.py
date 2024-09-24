class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.head = [0, 0]
        self.width = width
        self.height = height
        self.food = food
        self.block = set()
        self.dir = {"R": [0, 1], "L": [0, -1], "D": [1, 0], "U": [-1, 0]}
        self.Revdir = {"R": [0, -1], "L": [0, 1], "D": [-1, 0], "U": [1, 0]}
        self.score = 0
        self.foodIdx = 0
        self.gameOver = False
        self.moves = []


    def addSnakeBody(self):
        curr = self.head

        for i in range(len(self.moves) - 1, len(self.moves) - self.score, -1):
            curr = [curr[0] + self.Revdir[self.moves[i]][0], curr[1] + self.Revdir[self.moves[i]][1]]
            self.block.add((curr[0], curr[1]))


    def move(self, direction: str) -> int:
        if self.gameOver:
            return -1
        newposition = [self.head[0] + self.dir[direction][0], self.head[1] + self.dir[direction][1]]
        self.head = newposition
        if (newposition[0], newposition[1]) in self.block or newposition[0] < 0 or newposition[0] >= self.height or  newposition[
            1] < 0 or newposition[1] >= self.width:
            self.gameOver = True
            return -1
        self.moves.append(direction)
        if self.foodIdx < len(self.food) and newposition[0] == self.food[self.foodIdx][0] and newposition[1] == self.food[self.foodIdx][1]:
            self.foodIdx += 1
            self.score += 1
        self.block = set()
        self.addSnakeBody()
        # print(direction,self.block)
        # print()
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
