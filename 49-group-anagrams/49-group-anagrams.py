class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # https://stackoverflow.com/questions/8181513/finding-and-grouping-anagrams-by-python
        return [list(g)for k,g in itertools.groupby(sorted(strs,key=sorted),sorted)]