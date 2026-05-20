class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        seen = set()
        island = 0

        def bfs(r , c):
            if r == rows and c == cols:
                return False
            
            q = collections.deque()
            q.append((r , c))
            seen.add((r , c))

            directions = [[1 , 0] , [0 , 1] , [-1 , 0] , [0 , -1]]

            while q:
                row , col = q.popleft()

                for dr , dc in directions:
                    nr , nc = dr + row , dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr , nc) not in seen:
                        seen.add((nr , nc))
                        q.append((nr , nc))
            return True
        for r in range(rows):
            for c in range(cols):
                if (r , c) not in seen and grid[r][c] != "0":
                    if bfs(r , c):
                        island += 1
        return island 




