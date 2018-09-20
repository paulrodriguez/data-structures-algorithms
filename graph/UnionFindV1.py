class UnionFind:
    def __init__(self,nodes):
        self.parent = [ _ for _ range(nodes)]

    def find(self,v):
        if self.parent[v]!=v:
            return self.find(self.parent[v])

        return self.parent[v]

    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)

        self.parent[xroot] = yroot
