class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        ref = strs[0]
        res = ""

        for i in range(len(ref)):
            ptr = 1
            temp = ""
            match = False
            while ptr < len(strs):
                if i < len(strs[ptr]) and ref[i] == strs[ptr][i]:
                    ptr += 1
                    match = True
                else:
                    match = False
                    break
            
            if match:
                res += ref[i]
            
            else:
                break
        print(res)
        return res
