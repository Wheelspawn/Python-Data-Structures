class Queue(object):
    def __init__(self,queue=[]): # FIFO-enforced list
        self.queue=queue[:]

    def enqueue(self, v):
        self.queue.append(v)

    def dequeue(self):
        v = self.queue[0]
        self.queue.remove(self.queue[0])
        return v

    def peek(self):
        return self.queue[0]
