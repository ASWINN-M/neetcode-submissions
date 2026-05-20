class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        str1 = "".join(ch for ch in s if ch.isalnum())
        
        if str1 == str1[::-1]:
            return True
        return False