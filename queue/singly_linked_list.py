class Node:
    def __init__(self, value=None, next_node=None):
    
        self.value = value
        
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
       
        self.next_node = new_next
class LinkedList:
    def __init__(self):
        self.head: Node = None  
        self.tail: Node = None  
        self.length = 0
    def __str__(self):
        pass

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
######################################################################
   
    def add_to_tail(self, value):
        if self.tail is None:     
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next_node = new_tail
            self.tail = new_tail
        self.length += 1
######################################################################
    def remove_head(self):
        if self.head is None: 
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next_node
            self.length = self.length - 1
            return current_head.value
######################################################################  
    def remove_tail(self):
        if self.tail is None:
            return None
        value = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = None
            self.tail = current

        return value




        
