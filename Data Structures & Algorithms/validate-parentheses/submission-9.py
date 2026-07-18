class Solution:
    def isValid(self, s: str) -> bool:
        brac = {"{":"}" , "[":"]" , "(":")"}
        res = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                res.append(i)
            
            else:
                if not res or brac[res.pop()] != i:
                    return False
                

    
        if len(res) > 0:
            return False
        return True
            