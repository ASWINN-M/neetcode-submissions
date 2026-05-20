class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
                stack = collections.deque()
                res = [0] * len(temperatures)
                count = 0
                for i , v in enumerate(temperatures):
                        while stack and temperatures[stack[-1]] < v:
                                j = stack.pop()
                                res[j] = i - j
                        stack.append(i)
                        
                return res
                                                                                                                                                                        

                                                                                                                                                                                

                                                                                                                                                                                        