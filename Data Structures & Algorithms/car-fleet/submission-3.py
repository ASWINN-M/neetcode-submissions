class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rel_pos = []
        for s , p in zip(speed , position):
            rel_pos.append((p , s))
        rel_pos.sort()
        print(rel_pos)
        time = collections.deque()
        fleet = 1 if rel_pos else 0
        
        for i in range(len(rel_pos) - 1, -1 , -1):
            temp = (target - rel_pos[i][0]) / rel_pos[i][1]
            if not time or temp > time[-1]:
                fleet += 1
                time.append(temp)
            
        return fleet - 1


        
            
