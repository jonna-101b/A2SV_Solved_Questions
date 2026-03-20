class Solution:
    def __init__(self) -> None:
        self.stack = []

    def add(self) -> None:
        while len(self.stack) > 1 and self.stack[-2][1]:
            popped, boolean = self.stack.pop()
            self.stack[-1][0] += popped
            self.stack[-1][1] = True

    def multiply(self) -> None:
        if len(self.stack) > 1: 
            popped, boolean = self.stack.pop()
            self.stack[-1][0] *= popped
            self.stack[-1][1] = True

    def scoreOfParentheses(self, s: str) -> int:
        prevClosed = False
        prevOpen = False

        for char in s:
            if char == "(":
                if prevOpen:
                    self.stack[-1][0] += 1
                    self.stack[-1][1] = False

                self.stack.append([1, True])
                prevClosed = False
                prevOpen = True

            else:
                if prevClosed:
                    self.multiply()
                    self.add()
                else:
                    self.add()
                
                prevClosed = True
                prevOpen = False

        return self.stack[0][0]