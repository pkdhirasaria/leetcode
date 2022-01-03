class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        from datetime import datetime
        for i in range(len(keyName)):
            d[keyName[i]].append(keyTime[i])
        # print(sorted(d.items(),key=lambda x: x[1]))
        print(d)
        ans = []
        for key in sorted(d.keys()):
            entry_time = sorted(d[key])
            count = 0
            if len(entry_time) >= 3:
                i = 0
                # j = 1
                k = 2
                while k < len(entry_time):
                    t2 = datetime.strptime(entry_time[k],'%H:%M')
                    t1 = datetime.strptime(entry_time[i],'%H:%M')
                    diff = (t2 - t1).total_seconds()
                    if diff <=3600:
                        ans.append(key)
                        break
                        #Alert
                    else:
                        i += 1
                        k += 1
        return ans