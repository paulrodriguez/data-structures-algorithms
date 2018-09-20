from MinHeap import MinHeap

h = MinHeap()
h.insert(7)
h.insert(5)
h.insert(11)
h.insert(2)
h.insert(15)
h.insert(18)
h.insert(22)

print(h.heap)

h.decreaseKey(5,1)
print(h.heap)
h.deleteKey(4)
print(h.heap)
