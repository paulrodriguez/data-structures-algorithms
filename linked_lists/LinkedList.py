from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    
    #insert to end of list
    def insert(self,val):
        if self.head == None:
            self.head = Node(val)
            return

        
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next

        tmp.next = Node(val)

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

