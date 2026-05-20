class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = collections.deque()
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        res = []
        for i in stack:
            res.append(i)
        return res
        
            