class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_s1 , hash_s2 = defaultdict(int) , defaultdict(int)
        for i in s1:
            hash_s1[i] = hash_s1.get(i , 0) + 1
        print(hash_s1)
        l = 0
        for i in range(len(s1)):
            hash_s2[s2[i]] += 1
        print(hash_s2)
        r = len(s1) - 1
        while r < len(s2):
            if hash_s1 == hash_s2:
                return True
            r += 1
            if r == len(s2):
                break
            hash_s2[s2[l]] -= 1
            if hash_s2[s2[l]] == 0:
                del hash_s2[s2[l]]
            l += 1
            hash_s2[s2[r]] += 1
            

            
            print(hash_s2)
            print(hash_s1)
            
        return False


        
        

        
