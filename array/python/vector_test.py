import unittest
from Vector import Vector

class VectorTest(unittest.TestCase):
    def test_vector_init(self):
        vector = Vector()
        self.assertIsInstance(vector,Vector)
        self.assertEquals(-1,vector.last)
        self.assertEquals(0,vector.size)

    def test_capacity(self):
        vector = Vector()
        self.assertEquals(2,vector.capacity)
        
        vector.increaseCap()
        self.assertEquals(4,vector.capacity)

    def test_push_back(self):
        vector = Vector()
        vector.push_back(5)
        self.assertEquals(1,vector.getSize())
        vector.push_back(6)
        vector.push_back(7)
        self.assertEquals(3,vector.getSize())
        self.assertEquals(4,vector.capacity)
        self.assertEquals(2,vector.last)

    def test_pop_back(self):
        vector = Vector()
        vector.push_back(1)
        vector.push_back(2)
        vector.push_back(3)
        self.assertEquals(3,vector.pop_back())
        self.assertEquals(2,vector.getSize())
        self.assertEquals(1,vector.last)
        self.assertEquals(4,vector.capacity)
        
        self.assertEquals(2,vector.pop_back())
        self.assertEquals(1,vector.pop_back())

        self.assertEquals(None,vector.pop_back())

        
    def test_push_front(self):
        vector = Vector()
        vector.push_front(1)
        vector.push_front(2)
        vector.push_front(3)
        
        self.assertEquals(3,vector.get(0))
        self.assertEquals(3,vector.getSize())
        self.assertEquals(2, vector.last)
        self.assertEquals(4,vector.capacity)

        self.assertEquals(3,vector.pop_front())
        self.assertEquals(2,vector.get(0))
        self.assertEquals(1,vector.get(1))
        self.assertEquals(None,vector.get(2))
       

        self.assertEquals(2,vector.pop_front())
        self.assertEquals(1,vector.pop_front())
        self.assertEquals(None,vector.pop_front()) 

    def test_insert_at(self):
        vector = Vector()
        vector.insertAt(5,5)
        self.assertEquals(0,vector.getSize())

if __name__=='__main__':
    unittest.main()
