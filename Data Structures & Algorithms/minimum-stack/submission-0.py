class MinStack:
    # second stack to track the min values
    # optimal: stack to store the diff between the pushed value and the current min
    # a negative stored value means the top value is min, so when it is popped, min needs update (restore)
    def __init__(self):
        self.stack = []
        self.min = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val 
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return 

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min



    def getMin(self) -> int:

        return self.min
        
