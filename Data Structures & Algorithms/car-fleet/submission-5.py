class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rel_pos = []
        for s , p in zip(speed , position):
            rel_pos.append((p , s))
        rel_pos.sort()
        print(rel_pos)
        time = collections.deque()
        fleet = 0
        
        for i in range(len(rel_pos) - 1, -1 , -1):
            temp = (target - rel_pos[i][0]) / rel_pos[i][1]
            time.append(temp)
            if len(time) >= 2 and time[-1] <= time[-2]:
                time.pop()
                
            
        return len(time)


        
            
