class Solution:
    def minAvailableDuration(self, a: List[List[int]], b: List[List[int]], duration: int) -> List[int]:
        a.sort(key=lambda x : x[0])
        b.sort(key=lambda x : x[0])
        print(a,b)
        i =0
        j = 0
        while i < len(a) and j < len(b):
            if a[i][1] >= b[j][0]:
                x = max(a[i][0],b[j][0])
                y = min(a[i][1],b[j][1])
                if y-x >= duration:
                    return [x,x+duration]
                if a[i][1] <= b[j][1]:
                    i += 1
                else:
                    j += 1
            else:
                i += 1
        return []