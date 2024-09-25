class Trie:
    
    def __init__(self):
        self.children = dict()
        self.sum = 0
        self.isEnd = False
    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        root = Trie()
        
        def insert(word):
            curr = root
            for w in word:
                if w not in curr.children.keys():
                    curr.children[w] = Trie()
                curr.children[w].sum += 1
                curr = curr.children[w]
            curr.isEnd = True
        
        def getScore(word):
            val = 0
            curr = root
            for w in word:
                val += curr.children[w].sum
                curr = curr.children[w]
            return val
        
        for word in words:
            insert(word)
        ans = []
        for word in words:
            ans.append(getScore(word))
        return ans
                
