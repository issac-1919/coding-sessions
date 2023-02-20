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
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while (current_node.next is not None):
            current_node = current_node.next
        
        current_node.next = node
    
    def set_after(self, data, prev_data):
        
        if prev_data is None:
            print("Given data must be present in the linked list\n")
            return

        prev_ = self.head
        node = Node(data)
        while prev_.next is not None:
            if prev_.data == prev_data:
                prev_ = node
                break
            prev_ = prev_.next
        
        node.next = prev_.next
        prev_.next = node

    def set_at(self, data, pos=0):
        node = Node(data)
        idx = 0
        current_node = self.head
        while current_node.next:
            if pos == idx:
                break
            current_node = current_node.next
            idx += 1
        node.next = current_node.next
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