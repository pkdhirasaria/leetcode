class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        return sum([1 if a!=b else 0 for a,b in zip(s1,s2)]) == 2