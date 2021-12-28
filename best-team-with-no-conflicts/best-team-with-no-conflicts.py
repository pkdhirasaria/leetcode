class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        l = []
        for a,b in zip(scores,ages):
            l.append([a,b])
        # print(sorted(l))
        l.sort(key=lambda x:(x[1], x[0]))
        # print(l)
        dp = [-1] * len(l)
        for i in range(len(l)):
            dp[i] = l[i][0]
        # dp[len(l)-1] = l[-1][1]
        for i in range(len(l)):
            high_score = l[i][0]
            for j in range(i-1,-1,-1):
                if l[i][0] >= l[j][0]:
                    dp[i] = max(dp[i],dp[j] + l[i][0])
                    
                # high_score = max(high_score,l[j][0])
        # print(dp)
        return max(dp)