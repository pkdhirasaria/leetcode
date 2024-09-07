class HitCounter:

    def __init__(self):
        self.a = []

    def hit(self, timestamp: int) -> None:
        self.a.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if  not self.a or self.a[-1] < timestamp - 300:
            return 0
        l = 0
        h = len(self.a)-1
        mid = -1
        while l <= h:
            mid = (l+h)//2
            if self.a[mid] > timestamp - 300:
                h = mid-1
            else:
                l = mid + 1
        return len(self.a) - l









# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)