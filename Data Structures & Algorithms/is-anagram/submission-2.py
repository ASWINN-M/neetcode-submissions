class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_hash = {}
        if len(s) != len(t):
            return False
        for i in t:
            if i in t_hash:
                t_hash[i] += 1
            else:
                t_hash[i] = 1
        print(t_hash)
        for i in s:
            if i in t_hash:
                if t_hash[i] > 0:
                    t_hash[i] -= 1
                else:
                    return False
            else:
                return False
        if sum(t_hash.values()) >= 1:
            return False
        return True 