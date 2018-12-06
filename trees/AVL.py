class Node:
    def __init(self,v,left=None,right=None):
        self.v = v
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None

    def insert(self,val):
        self.root = insertUtil(val,self.root)

    def insertUtil(self,val,root):
        if root == None:
            return Node(val)

        
