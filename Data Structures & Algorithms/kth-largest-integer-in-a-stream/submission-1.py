class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        nums = self.nums
        nums.sort()
        k = self.k
        r = len(nums)
        while k > 0:
            k -= 1
            r -= 1
        return nums[r]
