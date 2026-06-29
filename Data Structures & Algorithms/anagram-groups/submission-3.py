class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for i in s:
                count[ord('a') - ord(i)] += 1

            res[tuple(count)].append(s)
        
        grp = []

        for v in res.values():
            grp.append(v)
        
        return grp