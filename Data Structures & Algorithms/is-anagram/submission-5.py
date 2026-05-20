class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_hash = {}
        s_hash = {}
        for i in range(len(t)):
            t_hash[t[i]] = 1 + t_hash.get(t[i],0)
            s_hash[s[i]] = 1 + s_hash.get(s[i],0)
        if s_hash == t_hash:
            return True
        return False