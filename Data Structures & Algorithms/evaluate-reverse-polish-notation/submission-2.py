class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()

        for token in tokens:
            if token == "+":
                n1 , n2 = stack.pop() , stack.pop()
                stack.append(int(n1) + int(n2))
            elif token == "-":
                n1 , n2 = stack.pop() , stack.pop()
                stack.append(int(n2) - int(n1))
            elif token == "*":
                n1 , n2 = stack.pop() , stack.pop()
                stack.append(int(n1) * int(n2))
            elif token == "/":
                n1 , n2 = stack.pop() , stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(token))
        return stack[0]