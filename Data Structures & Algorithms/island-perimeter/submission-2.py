class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land = 0
        rows , cols = len(grid) , len(grid[0])
        seen = set()
        def bfs(r , c , land):
            q = collections.deque()
            q.append((r , c))
            seen.add((r , c))
            directions = [[1 , 0] , [0 , 1] , [-1 , 0] , [0 , -1]]
            while q:
                row , col = q.popleft()
                for dr , dc in directions:
                    nr , nc = row + dr , col + dc
                    if nr < 0 or nr >= rows or 0 > nc or nc >= cols or grid[nr][nc] == 0:
                        land += 1
                    elif (nr , nc) not in seen:
                        seen.add((nr , nc))
                        q.append((nr , nc))    
            return land
        
        for r in range(rows):
            for c in range(cols):
                if (r , c) not in seen and grid[r][c] != 0:
                    res = bfs(r , c , land)
        return res if res != 0 else 0