class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l , r = 0 , 0
        res = []

        while r < len(nums):
            #popping if the element is smaller
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            #we need to add the right elements to the queue
            q.append(r)
            if l > q[0]:
                q.popleft()
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res


