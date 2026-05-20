class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 , count_s2 = [0] * 26 , [0] * 26
        if len(s1) > len(s2):
            return False
        for alp in s1:
            count_s1[ord(alp) - ord('a')] += 1
        l = 0
        
        for r in range(len(s2)):
            count_s2[ord(s2[r]) - ord('a')] += 1
            # if count_s1[ord(s2[r]) - ord('a')] == 0:
            #     count_s2[ord(s2[r]) - ord('a')] -= 1
            #     l += 1
            if count_s1 == count_s2:
                return True
            if r - l + 1 >= len(s1):
                count_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            else:
                continue
            
            
        return False
        
        

        
