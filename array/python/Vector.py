import unittest
# common methods for vectors
# push to end of array
# get value at specified position
# delete at specified index
# delete from head
# delete from tail
# push at start of array
# insert at specified index
class Vector:
    def __init__(self):
        self.capacity = 2
        self.array = [None]*self.capacity
        self.last = -1
        self.size = 0

    def getSize(self):
        return self.size

    def increaseSize(self):
        self.size += 1
        return

    def decreaseSize(self):
        self.size -= 1
        return

    
    # double the capacity of vector
    def increaseCap(self):
        self.capacity = self.capacity*2
        tmp = [None]*self.capacity
        for i,v in enumerate(self.array):
            tmp[i] = v
        self.array = tmp

    # remove and return value at end of array
    def pop_back(self):
        if self.getSize()==0:
            print('vector is empty')
            return
        tmp = self.array[self.last]
        self.array[self.last] = None
        self.last -= 1
        self.decreaseSize()
        return tmp

    # insert new value to the beginning of the array    
    def push_back(self,val):
        if self.getSize()==self.capacity:
            self.increaseCap()
        self.last += 1
        self.array[self.last] = val
        self.increaseSize()

    # remove element at the beginning of the array
    def pop_front(self):
        if self.getSize()==0:
            print('vector is empty')
            return

        tmp = self.array[0]
        j = 1
        while j <=self.last:
            self.array[j-1] = self.array[j]
            j += 1

        self.array[self.last] = None
        self.last -= 1
        self.decreaseSize()

        return tmp

    # add element at beginning of array
    def push_front(self,val):
        if self.getSize()==self.capacity:
            self.increaseCap()

        self.last += 1

        j = self.last
        while j >=1:
            self.array[j] = self.array[j-1]
            j -= 1
        
        self.array[0] = val
        self.increaseSize()

    # obtain element at a certain position
    def get(self,idx):
        if idx>=0 and self.getSize():
            return self.array[idx]

        print('invalid index')
        return

    # insert element at specified position
    def insertAt(self,idx,val):
        if idx<0 or idx >= self.getSize():
            print('invalid position')
            return

    def deleteAt(self,idx,val):
        if idx<0 or idx>=self.getSize():
            print('invalid position')
            return
