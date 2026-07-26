class StockSpanner:

    def __init__(self):
        self.stack = []
        self.res = [] 
    def next(self, price: int) -> int:
        span = 1
        stack = self.stack
        while stack and stack[-1][0] <= price:
            span += stack[-1][1]
            stack.pop()
        
        stack.append([price , span])
        self.res.append(span)
        return self.res[-1]

            
            
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)