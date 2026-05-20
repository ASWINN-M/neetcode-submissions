class FreqStack:

    def __init__(self):
        self.stack = collections.defaultdict(list)
        self.freq = {}
        self.max_val = 0
    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val , 0) + 1

        if self.freq[val] > self.max_val:
            self.max_val = self.freq[val]
        
        self.stack[self.freq[val]].append(val)

        


    def pop(self) -> int:
        v = self.stack[self.max_val].pop()

        self.freq[v] -= 1

        if not self.stack[self.max_val]:
            self.max_val -= 1
        
        return v

        
        # for i in range(len(keys) -1 , -1 , -1):

        
    


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()