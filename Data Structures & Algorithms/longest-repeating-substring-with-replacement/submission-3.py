class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(count.values())
            windowLen = r - l + 1
            while l < len(s) and windowLen - maxf > k:
                count[s[l]] -= 1
                l += 1
                maxf = max(count.values())
                windowLen -= 1
            res = max(res , r - l + 1)

        return res


        
        

        
        
        
            
        
        
            