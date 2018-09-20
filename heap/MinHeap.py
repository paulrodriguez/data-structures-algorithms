class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)
    
    def left(self, i):
        return (2*i + 1)

    def right(self, i):
        return (2*i + 2)
   
 
    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    # swaps node with its parent if it does not
    # satisfy the heap property
    def siff(self,i):
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            j = self.parent(i)
            self.swap(i,j)
            i = j
    
    def insert(self,val):
        self.heap.append(val)
        self.siff(len(self.heap) - 1)

    def getMin(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def extractMin(self):
        if len(self.heap) > 0:
            min_key = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.heapify(0)
            
            return min_key
        else:
            return None
    
    def decreaseKey(self, i, val):
        self.heap[i] = val
        self.siff(i)
    
    def deleteKey(self, i):
        self.heap[i] = float('-inf')
        self.siff(i)
        self.extractMin()

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        small = i
        if l < len(self.heap) and self.heap[l] < self.heap[small]:
            small = l

        if r < len(self.heap) and self.heap[r] < self.heap[small]:
            small = r

        if small != i:
            self.swap(small,i)
            self.heapify(small)

