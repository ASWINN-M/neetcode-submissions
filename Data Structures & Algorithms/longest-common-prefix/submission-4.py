class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]   
        j = len(check) 
        for k in range(1, len(strs)):
            i = 0
            while i < min(len(check ), len(strs[k])):
                if check[i] != strs[k][i]:
                    break
                i += 1 
            j = min(i,j)
        return check[ : j]
