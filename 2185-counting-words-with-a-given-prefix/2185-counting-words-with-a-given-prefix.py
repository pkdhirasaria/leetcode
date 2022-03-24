class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        d = {}
        for word in words:
            s = ""
            for w in word:
                s += w
                d[s] = d.get(s,0) + 1
        return d.get(pref,0)