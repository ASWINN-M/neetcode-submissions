class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()

        for token in tokens:
            if token == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            
            elif token == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            
            elif token == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            
            elif token == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                if n1 != 0:
                    stack.append(int(n2 / n1))
                else:
                    stack.append(0)
            else:
                stack.append(int(token))
        return stack[0]