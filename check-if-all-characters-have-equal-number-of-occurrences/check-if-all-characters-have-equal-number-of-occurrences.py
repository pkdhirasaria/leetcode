class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        t = set()
        for v in counter.values():
            t.add(v)
        return True if len(t) == 1 else False
            