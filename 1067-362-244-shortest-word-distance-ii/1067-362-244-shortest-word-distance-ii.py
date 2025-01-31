class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict
        

    def shortest(self, word1: str, word2: str) -> int:
        ans = float('inf')
        d1 = -1
        d2 = -1
        for i in range(len(self.words)):
            if self.words[i] == word1:
                d1 = i
                if d2 != -1:
                    ans = min(ans,abs(d1-d2))
            if self.words[i] == word2:
                d2 = i
                if d1 != -1:
                    ans = min(ans,abs(d1-d2))
        return ans



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)