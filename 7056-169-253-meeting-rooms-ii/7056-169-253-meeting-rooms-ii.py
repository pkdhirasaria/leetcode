class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start , end = [],[]
        for a,b in intervals:
            start.append(a)
            end.append(b)
        start.sort()
        end.sort()
        room = 0
        i = 0
        j =0
        n = len(start)
        print(start, end)
        while i < n and j < n:
            if start[i] < end[j]:
                i += 1
                room +=1
            else:
                j += 1
                i += 1
        return room
