from FloydWarshall import FloydWarshall

graph = [[0,5,float('inf'),10],[float('inf'),0,3,float('inf')],
[float('inf'),float('inf'),0,1],[float('inf'),float('inf'),float('inf'),0]]

fw = FloydWarshall(graph,4)

fw.solve()
