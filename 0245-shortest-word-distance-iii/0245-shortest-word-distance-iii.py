class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = False
        w2 = False
        i = -1
        j = -1
        ans = float('inf')
        for k in range(len(wordsDict)):
            if word1 == word2 and wordsDict[k] == word1:
                if not w1:
                    i = k
                    w1 = True
                    w2 = False
                elif not w2:
                    j = k
                    w2 = True
                    w1 = False
            elif wordsDict[k] == word1:
                i = k
            elif wordsDict[k] == word2:
                j = k
            if i!=-1 and j != -1:
                ans = min(ans,abs(i-j))
        return ans
        