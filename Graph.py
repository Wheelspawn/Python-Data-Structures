class Graph(object):
    def __init__(self, vertices=[], edges=[]):
        self.vertices=vertices[:]
        self.edges=edges[:]

    def add(self, n):
        if type(n) != Vertex:
            print("Value error")
        else:
            n.g = self
            self.vertices.append(n)
            
        # self.manageAdj()

    def delete(self, n):
        if n in self.vertices == False:
            print("Vertex not present in graph, nothing to delete")
        else:
            for v in self.vertices:
                if n in v.edges:
                    v.edges.remove(n)
                
            self.vertices.remove(n)
            # self.manageAdj()

    def addEdge(self, x, y, dist):
        self.edges.append(Edge(x,y,dist))
        x.edges.append([y,dist])
        y.edges.append([x,dist])

    def removeEdge(self, x, y, dist):
        for edge in self.edges:
            if edge.x == x and edge.y == y:
               self.edges.remove(Edge(x,y,dist))
        x.edges.remove([y,dist])
        y.edges.remove([x,dist])

    '''
    def manageAdj(self):
        self.adj=[]
        self.adj.extend([[0 for i in range(len(self.vertices))]
                            for j in range(len(self.vertices))])
        
        for v in self.vertices:
            for w in v.edges:
                self.adj[self.vertices.index(v)][self.vertices.index(w)] = 1
    '''
            
    def printout(self):
        for v in self.vertices:
            print(str(v))

    def printAdj(self):
        for row in self.adj:
            print(row)

    def BFT(self, start, d=1): # breadth-first traversal # breadth-first traversal
        t = [start]
        for edge in start.edges:
            t.append(edge[0])
        print(t)

        for edge in t:
            print('hi')

        '''
        t = []
        if self.isRoot() == True: # root is first in list
            t = [self]
            
        for c in self.child: # add children
            t.append(c)
                
        for c in t: # for children of children
            if c.depth != 0: # end of recursive depth
                t.extend(c.BFS(d+1)) # add next nodes to list with +1 level of depth
        return t
        '''

    
class WeightedGraph(Graph):
    def __init__(self, vertices=[], adj=[]):
        self.vertices=vertices[:]
        self.adj=adj[:]      

class Vertex(object):
    def __init__(self,name="",edges=[],color='w',pred=None,element=None):
        self.name=name
        self.edges=edges[:]
        self.color=color
        self.pred=pred
        self.element=element

    def addEdge(self, vert, distance):
        l=self.edges.copy()
        l.append(vert)
        if (self in vert.edges) == False and (vert in l) == True:
            vert.edges.extend([self])
        self.edges=l
        

    def removeEdge(self, vert):
        l=self.edges.copy()
        
        if vert in l:
            l.remove(vert)
        if (self in vert.edges) == True and (vert in l) == False:
            vert.edges.remove(self)
            
        self.edges=l
    
    def printEdges(self):
        l = []
        for c in self.edges:
            l.append(c.name)
        return l

    def __str__(self):
        return "Node '" + self.name # + "' with edges " + str(self.printEdges())

    def __repr__(self):
        return "Node '" + self.name # + "' with edges " + str(self.printEdges())

class Edge(object):
    def __init__(self,x=None,y=None,distance=None,name=None):
        self.x=x
        self.y=y
        self.distance=distance
        self.name=str(x)+'-'+str(y)+'-'+str(distance)
        
    def __repr__(self):
        return "Edge from '" + self.x.name + "' to '" + self.y.name + "' with distance " + str(self.distance)

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

g=Graph()

a=Vertex("a")
b=Vertex("b")
c=Vertex("c")
d=Vertex("d")

g.add(a)
g.add(b)
g.add(c)
g.add(d)

g.addEdge(a,b,10)
g.addEdge(a,c,5)
g.addEdge(c,d,12)
