class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        # s = "0"* len(target)
        val = "0"
        count = 0
        for i in range(n):
            # print(i,val)
            if val != target[i]:
                val = "1" if val == "0" else "0"
                count += 1
        return count