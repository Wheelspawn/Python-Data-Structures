class Stack(object): # FILO-enforced list
    def __init__(self,stack=[]):
        self.stack=stack[:]

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        v = self.stack[-1]
        self.stack.remove(self.stack[-1])
        return v

    def peek(self):
        return self.stack[-1]
