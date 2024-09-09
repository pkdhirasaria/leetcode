class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        deadends = set([(int(de[0]), int(de[1]), int(de[2]), int(de[3])) for de in deadends])
        
        target = tuple(int(d) for d in target)
        q = deque()
        initial = tuple((0,0,0,0))
        q.append((initial,0))
        vis = set()
        vis.add(initial)
        while q:
            node, lvl = q.popleft()
            if node == target:
                return lvl
            for i in range(4):
                for delta in [1,-1]:
                    new_comp = list(node)
                    new_comp[i] = (new_comp[i] + delta) % 10
                    nc = tuple(new_comp)
                    # print(vis,new_comp,nc)
                    if nc not in vis and nc not in deadends:
                        vis.add(nc)
                        q.append((nc,lvl+1))
        return -1

                    