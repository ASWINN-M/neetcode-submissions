class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = [0] * 26
        
        for r in range(len(s)):
            windowlen = r - l + 1
            freq[ord(s[r]) - ord('A')] += 1
            
            while l < r and windowlen - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                windowlen = r - l + 1
            
            res = max(res , r - l + 1)

        return res
