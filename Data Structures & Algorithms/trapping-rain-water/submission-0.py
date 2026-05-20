class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft , maxRight = [height[0]] , [height[-1]]
        
        for i in range(1 , len(height)):
            if maxLeft[-1] < height[i]:
                maxLeft.append(height[i])
            else:
                maxLeft.append(maxLeft[-1])
        for i in range(len(height) - 2, -1, -1):
            if maxRight[-1] < height[i]:
                maxRight.append(height[i])
            else:
                maxRight.append(maxRight[-1])

        trapped = 0
        maxRight.reverse()
        print(maxRight , maxLeft)
        for i in range(len(height)):
            if min(maxLeft[i] , maxRight[i]) - height[i] >= 0:
                trapped += min(maxLeft[i] , maxRight[i]) - height[i]

        return trapped
        