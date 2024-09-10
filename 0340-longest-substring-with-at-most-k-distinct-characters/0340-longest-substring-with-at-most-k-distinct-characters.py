class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        track = set()
        d = defaultdict(int)
        i = 0
        j = 0
        ans = 0
        n = len(s)
        while j < n:
            track.add(s[j])
            d[s[j]] += 1
            if len(track) > k:
                # track.discard(s[j])
                ans = max(ans, j - i)
                while i < n and len(track) != k:
                    if d[s[i]] == 1:
                        track.discard(s[i])
                        d[s[i]] = 0
                    else:
                        d[s[i]] -= 1
                    i += 1
            j += 1
        ans = max(ans, j - i)
        return ans