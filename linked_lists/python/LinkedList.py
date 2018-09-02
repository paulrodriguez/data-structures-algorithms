from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    #insert to beginning of list
    def insertBeginning(self,val):
        n = Node(val)
        n.next = self.head
        self.head = n

        return self.head

    #insert to end of list
    def insertEnd(self,val):
        if self.head == None:
            self.head = Node(val)
            return

        
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next

        tmp.next = Node(val)

        return self.head
    
    # insert value at certain position
    # the position is zero-indexed
    def insertAt(self,pos, val):
        index = 0
        tmp = self.head
        prev = None
        while tmp != None:
            if pos == index:
                node = Node(val)
                node.next = tmp
                if prev != None:
                    prev.next = node
                return node

            index += 1
            prev = tmp
            tmp = tmp.next

        #if no position could be found, return none
        return None

    def getSize(self):
        count = 0
        n = self.head
        while n != None:
            n = n.next
            count+=1
        
        return count
    
    # delete at specified position
    # using 0-based indexing
    def deleteAt(self,pos):
        if self.head == None:
            print('no value found at: ' + str(pos))
            return False

        tmp = self.head
        prev = None
        index = 0
        while tmp != None:
            if pos == index:
                if prev == None:
                    self.head = tmp.next
                else:
                    prev.next = tmp.next
                return True

            prev = tmp
            tmp = tmp.next
            
            index += 1 
        print('no value found at: ' + str(pos))
        return False
    def delete(self,val):
        # base case, empty list
        if self.head == None:
            print('no value found: ' + str(val))
            return False

        tmp = self.head
        prev = None

        while tmp!=None:
            if tmp.val == val:
                if prev == None:
                    self.head = tmp.next
                else:
                    prev.next = tmp.next
                return True
            prev = tmp
            tmp = tmp.next
        
        # if we get here, it means a value could not be found
        print('no value found: ' + str(val))
        return False

    def print_list(self):
        tmp = self.head
        linked_list = ''
        while tmp!=None:
            linked_list += str(tmp.val)
            if tmp.next != None:
                linked_list += ' -> '
            tmp = tmp.next
        
        print(linked_list)

