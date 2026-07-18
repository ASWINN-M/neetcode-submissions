class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = 0
        
        hash_t , hash_s = defaultdict(int) , defaultdict(int)
        res = float("inf")
        start = 0
        for i in t:
            hash_t[i] += 1
        
        l = 0
    
        for r in range(len(s)):
            if s[r] in hash_t:
                hash_s[s[r]] += 1
                if hash_s[s[r]] == hash_t[s[r]]:
                    count += 1
                    while count == len(hash_t):
                        if res > r - l + 1:
                            res = r - l + 1
                            start = l
                        if s[l] in hash_t:
                            hash_s[s[l]] -= 1
                            if hash_s[s[l]] < hash_t[s[l]]:
                                count -= 1  

                            l += 1
                        else:
                            l += 1
                        
        
        return s[start : start + res] if res != float("inf") else ""
                
                    


                        
                

