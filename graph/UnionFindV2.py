class Unionfind:
    def __init__(self,nodes):
        self.parent = [ _ for _ in range(nodes)]
        self.rank = [0 for _ in range(nodes)]

    def find(self,v):
        if self.parent[v]!=v:
            self.parent[v] = self.find(parent[v])
        return self.parent[v]

    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[yroot] < self.rank[xroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[xroot] = yroot
            self.rank[yroot] += 1
