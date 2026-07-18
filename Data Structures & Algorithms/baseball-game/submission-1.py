class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = collections.deque()
        
        for i in operations:
            if i == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2)
                stack.append(n1)
                stack.append(n1 + n2)
            elif i == "C":
                stack.pop()
            
            elif i == "D":
                n1 = stack.pop()
                stack.append(n1)
                stack.append(n1 * 2)
            else:
                
                stack.append(int(i))
        
        return sum(stack)
            
                