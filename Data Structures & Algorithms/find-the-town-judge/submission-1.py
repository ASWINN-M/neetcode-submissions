class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        seen = set()
        for i , j in trust:
            seen.add(j)
        n = 0
        for s in seen:
            n = s
        if len(seen) == 1:
            return n 
        return -1