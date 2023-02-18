class Node:
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next

class singly_llist:
    def __init__(self):
        self.head = None
    
    def set_at_front(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def set_at_rear(self, data):
        node = Node(data, self.head)
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
    
    def display_singly(self):
            
        if self.head is None:
            return ("linked list is empty!") 
        
        llst = ''
        current_node = self.head
        while current_node is not None:
            llst += str(current_node.data) + "->"
            current_node = current_node.next
        llst = llst + 'None'
        return "Linked list:{}".format(llst)