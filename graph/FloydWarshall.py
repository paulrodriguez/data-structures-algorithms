class FloydWarshall:
    # for now store a matrix representation of a graph
    def __init__(self,graph,v):
        self.graph = graph
        self.v = v

    def solve(self):
        dist = [ [float('inf')]*self.v for _ in range(self.v)]
        
        # make copy of graph to keep track of distances    
        for idxx,v_from in enumerate(self.graph):
            for idx,v_to in enumerate(v_from):
                dist[idxx][idx] = v_to
    
        for k in range(self.v):
            for j in  range(self.v):
                for i in range(self.v):
                    dist[j][i] =  min(dist[j][i],dist[j][k]+dist[k][i])

        print(dist)
        # first loop iterates through all vertices to be picked as the intermediate vertex
        #for k in range(V):        

