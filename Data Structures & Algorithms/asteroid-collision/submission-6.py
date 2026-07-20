class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = collections.deque()
        alive = True
        for asteroid in asteroids:
            while stack and stack[-1] >= 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()

                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(asteroid)
            else:
                alive = True
            
            
        
        print(stack)

                

                
            

            
        res = []

        for i in stack:
            res.append(i)
        return res
        
            