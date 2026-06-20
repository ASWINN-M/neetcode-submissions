class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s , hash_t = {} , {}

        for i , j in zip(s , t):
            hash_s[i] = hash_s.get(i , 0) + 1
            hash_t[j] = hash_t.get(j , 0) + 1
        
        if hash_s == hash_t:
            return True
        return False