class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = collections.deque()
        path = path.split('/')
        print(path)
        for i in path:
            if i == "" or i == ".":
                continue
            if i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
            
        
        return "/" + "/".join(stack) 
        