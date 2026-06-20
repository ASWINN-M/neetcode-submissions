class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        ref = strs[0]
        res = ""
        for i in range(len(ref)):
            ptr = 1
            temp = ""
            match = True
            while ptr < len(strs):
                if i < len(strs[ptr]) and strs[ptr][i] == ref[i]:
                    ptr += 1
                else:
                    match = False
                    break
                
            if match:
                res += ref[i]
                
            else:
                break
        print(res)
        return res

