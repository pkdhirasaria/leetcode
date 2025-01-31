class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d1 = -1
        d2 = -1
        ans = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                d1 = i
                if d2 !=-1:
                    ans = min(ans,abs(d1-d2))
            if wordsDict[i] == word2:
                d2 = i
                if d1 !=-1:
                    ans = min(ans,abs(d1-d2))
        return ans
