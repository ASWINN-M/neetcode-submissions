class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = collections.deque()
        res = ""
        for i in path + "/":
            if i == "/":
                if res == "..":
                    if stack:
                        stack.pop()
                elif res != "" and res != ".":
                    stack.append(res)
                res = ""
            
            else:
                res += i

        
        return "/" + "/".join(stack)