class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = collections.deque()
        num = 0
        for i in s:
            
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == '[':
                stack.append(num)
                stack.append(i)
                num = 0
            elif i == ']':
                temp = ""
                while stack and stack[-1] != '[':
                    ele = stack.pop()
                    temp = ele + temp
                stack.pop()
                n = stack.pop()
                stack.append(temp * n)
            else:
                
                stack.append(i)
            
        
        return "".join(stack)
        
                 