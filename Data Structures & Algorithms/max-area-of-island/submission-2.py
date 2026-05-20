class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        island = 0
        seen = set()

        def bfs(r , c , area):
            q = collections.deque()
            q.append((r , c))
            seen.add((r , c))

            directions = [[1 , 0] , [0 , 1] , [-1 , 0] , [0 , -1]]

            while q:
                row , col = q.popleft()

                for dr , dc in directions:
                    nr , nc = row + dr , col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0 and (nr , nc) not in seen:
                        area += 1
                        seen.add((nr , nc))
                        q.append((nr , nc))
            return area

        for r in range(rows):
            for c in range(cols):
                if (r , c) not in seen and grid[r][c] != 0:
                    island = max(island , bfs(r , c , 1))
        return island