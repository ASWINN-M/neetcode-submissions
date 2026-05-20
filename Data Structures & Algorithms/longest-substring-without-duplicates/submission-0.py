class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ss = 0
        l = 0
        freq_map = {}
        for r in range(len(s)):
            if s[r] in freq_map:
                freq_map[s[r]] += 1

            else:
                freq_map[s[r]] = 1
            
            while freq_map[s[r]] > 1:
                freq_map[s[l]] -= 1
                l += 1
            
            max_ss = max(max_ss , r - l + 1)
        
        return max_ss