class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = set()
        sort_strs = [sorted(i) for i in strs]
        for i in range(len(sort_strs)):
            if i in seen:
                continue
            temp = [strs[i]]
            
            
            for j in range(i + 1 , len(sort_strs)):
                if sort_strs[i] == sort_strs[j]:
                    temp.append(strs[j])
                    seen.add(j)
            res.append(temp)
        
        print(res)
        return res
