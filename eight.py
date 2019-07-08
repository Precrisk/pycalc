'''
an attempt at creating and understanding linked list, circular linkes list doubly linked list.
'''
class Node:
   def __init__(self, data = None):
       self.data = data
       self.prev = None
       self.next = None
class DoubleLinkedList():
    def __init__(self):
        self.head = Node()
        self.head.next = self.head # self.head.next points to itself
        self.head.prev = self.head # self.head.prev points to itself
        self.size  = 1
    def insert_first_data(self, data):
        self.head.data = data
    def append(self, data):
        '''
        appends at the last position of this doubly linked list.
        '''
        temp = self.head.prev
        newnode = Node(data)
        newnode.prev = temp
        newnode.next = self.head
        self.head.prev = newnode
        newnode.prev.next = newnode
        self.size += 1
    def pop(self):
        oldnode = self.head.prev
        newnode = oldnode.prev
        self.head.prev = newnode
        newnode.next = self.head
        del oldnode
    def print(self, lead): # Function kept here because it makes the program easier to debug
        '''
        prints the data in the circular loop once
        '''
        curr = lead
        while curr.next != lead :
            print (curr.data)
            curr = curr.next
        print (curr.data)
class Round(DoubleLinkedList):
    def __init__(self, size):
        '''
        Initializes the Swordmen circle with no. of swordsmen inputted
        '''
        DoubleLinkedList.__init__(self)
        DoubleLinkedList.insert_first_data(self, 1)
        for n in range(2, size+1):
            DoubleLinkedList.append(self, n)
        self.curr = self.head
        # self.print(lead = self.curr) # Uncomment for better debugging
    def SolveRound(self):
        def kill_next(self):
            rm_node = self.curr.next
            repl_node = rm_node.next
            self.curr.next = repl_node
            repl_node.prev = self.curr
            print ('killed', rm_node.data)
            del rm_node
        def pass_sword(self):
            self.curr = self.curr.next
            print ('passed sword to', self.curr.data)
        for n in range(self.size-1):
            kill_next(self)
            pass_sword(self)
            # self.print(lead = self.curr) # Uncomment for better debugging
