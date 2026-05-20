class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":return ""
        l = 0 
        res = []
        countT = {}
        window = {}
        for i in range(len(s)):
            if s[i] in t:
                l = i
                break 
        for i in t:
            countT[i] = countT.get(i , 0) + 1
            window[i] = 0
        have ,need = 0, len(countT)

        for r in range(l , len(s)):
            if s[r] in window:
                window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                res.append((l , r))
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
                
        res1 = [r - l for l , r in res]
        idx = -1
        min_val = float('inf')
        for i in range(len(res1)):
            if res1[i] < min_val:
                idx = i
                min_val = res1[i]
        if idx != -1:
            return s[res[idx][0] : res[idx][1] + 1]
        return ""
         
                    
            

