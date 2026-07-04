class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = "".join(i for i in s if i.isalnum())
        return chars == chars[::-1]