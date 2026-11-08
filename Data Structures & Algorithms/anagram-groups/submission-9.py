class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #maos sorted anagram to all strs
        ans = defaultdict(list)
        for st in strs:
            
            s = sorted(st)
            tupleS = tuple(s)
            ans[tupleS].append(st)
        return list(ans.values())