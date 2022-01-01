class RLEIterator:

    def __init__(self, e: List[int]):
        self.en = e
        self.index = 0
        self.n = len(self.en)
        # print(self.en)

    def next(self, n: int) -> int:
        # print(self.index,n-self.en[self.index])
        if self.index >= self.n:
            return -1
        if self.en[self.index] == 0:
            self.index += 2
            if self.index >= self.n:
                return -1
        if self.en[self.index] >= n:
            self.en[self.index] -= n
            return self.en[self.index+1]
        while self.index < self.n and n > self.en[self.index]:
            n -= self.en[self.index]
            # if n <= self.en[self.index]:
            #     return self.en[self.index]
            self.index += 2
        if self.index < self.n:
            self.en[self.index] -= n
            return self.en[self.index+1]
        return -1
        # return a

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)