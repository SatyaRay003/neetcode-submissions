class MinStack:

    def __init__(self):
        self.stack = []  
        self.min_val = []      

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val:
            if val<=self.getMin(): # '=' is vital to allow duplicate minimum value
                self.min_val.append(val)
        else:
            self.min_val.append(val)
    
    def pop(self) -> None:
        if self.stack:
            if self.getMin()==self.stack[-1]:
                self.min_val.pop()
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        # min_val = self.stack[0]
        # for i in self.stack[1:]:
        #     if i<min_val:
        #         min_val=i
        # return min_val

        # return min(self.stack)

        return self.min_val[-1]
        
