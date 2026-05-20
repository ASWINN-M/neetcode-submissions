class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        similar = []
        res = []
        for i in strs:
            i = sorted(i)
            similar.append(i)
        same = {str(i) : [] for i in similar}

        for i in range(len(similar)):
            same[str(similar[i])].append(i)
        
        for key , val in same.items():
            temp = []
            for v in val: 
                temp.append(strs[v])
            res.append(temp)
        return res