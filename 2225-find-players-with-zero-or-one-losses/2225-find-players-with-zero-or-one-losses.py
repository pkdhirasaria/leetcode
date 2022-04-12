class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dw = defaultdict(int)
        dl = defaultdict(int)
        n = len(matches)
        match = set()
        for w,l in matches:
            dw[w] += 1
            dl[l] += 1
            match.add(w)
            match.add(l)
        answer = [[],[]]
        # print(dw,dl)
        for i in sorted(list(match)):
            if dl[i] == 0 and dw[i] > 0:
                answer[0].append(i)
            elif dl[i] == 1:
                answer[1].append(i)
        return answer