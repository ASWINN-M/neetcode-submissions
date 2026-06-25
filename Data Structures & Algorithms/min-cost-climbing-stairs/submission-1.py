class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def bfs(i):
            if i >= len(cost):
                return 1

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(bfs(i + 1) , bfs(i + 2))
            return memo[i]
        
        return min(bfs(0) , bfs(1)) - 1