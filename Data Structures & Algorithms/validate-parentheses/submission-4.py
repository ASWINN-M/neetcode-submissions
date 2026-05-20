class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        bracMap = {"}":"{" , "]":"[" , ")":"("}

        for i in s:
            if i == ")" or i == "}" or i == "]":
                if not stack or stack.pop() != bracMap[i]:
                        return False
            else:
                stack.append(i)
        
        if stack:
            return False
        return True

            