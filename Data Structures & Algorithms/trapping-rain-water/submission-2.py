class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft , maxRight = [0] , [0]
        left , right = height[0] , height[-1]
        for i in range(1 , len(height)):
            maxLeft.append(left)
            left = max(left , height[i])

        for i in range(len(height) - 2 , -1 , -1):
            maxRight.append(right)
            right = max(right , height[i])
        maxRight.reverse()
        res = 0
        for i in range(len(maxLeft)):
            res += max(0 , min(maxLeft[i] , maxRight[i]) - height[i])
        print(maxLeft , maxRight)
        return res


        