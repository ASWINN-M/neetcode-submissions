class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rel_pos = []
        for pos , sp in zip(position , speed):
            rel_pos.append((pos , sp))
        
        rel_pos.sort()
        fleet = 0
        stack = collections.deque()
        stack.append(float(target - rel_pos[-1][0]) / float(rel_pos[-1][1]))
        r = len(rel_pos) - 1
        while r >= 0:
            t = float(target - rel_pos[r][0]) / float(rel_pos[r][1])
            if t <= stack[-1]:
                fleet += 1
            else:
                stack.append(t)
            r -= 1
        return len(stack)


        
            
