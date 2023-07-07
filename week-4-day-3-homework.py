import string

class Node:
    
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f'<Node: {self.value}'
    


class LinkedList:
    
    def __init__(self, head_node_value):
        self.head = Node(head_node_value)
        
    def __repr__(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.value) #appends current_node's value to our nodes list
            current_node = current_node.right  #moves our current_node to the next node in the linked list.
        return f'<LinkedList: {" --> ".join(nodes)}>'
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right
    
    def append_node(self, value):
        new_node = Node(value)
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = new_node
    
    def print_list(self):
        nodes = []
        for node in self:
            nodes.append(str(node.value))
        print(" --> ".join(nodes))
        
        
class BST:
    
    def __init__(self, head_node_value):
        self.head_node = Node(head_node_value)
        self.sortedlist = []
        
    def add_node(self, value, node=None):
        new_node = Node(value)
        if not node: 
            node = self.head_node
        if value > node.value:
            if not node.right:
                node.right = new_node #if no node to the right, create it!
            else:
                self.add_node(value, node.right) #if there is no node to the right, we want to recursive call until new node can inst.
        elif value < node.value:
            if not node.left:
                node.left = new_node
            else:
                self.add_node(value, node.left)

    def print_in_order(self, node = None):
        if not node:
            node = self.head_node
        if node.left:
            self.print_in_order(node.left)
        self.sortedlist.append(node.value)
        print(node.value)
        if node.right:
            self.print_in_order(node.right)
    

# unsorted_list = [23,99,54,66,58,72,3,4,49,85]

bst = BST(58)
print(bst) 

bst.add_node(23)               
bst.add_node(99)               
bst.add_node(54)               
bst.add_node(66)               
bst.add_node(72)               
bst.add_node(3)               
bst.add_node(4)               
bst.add_node(49)               
bst.add_node(85)               
bst.add_node(90)               
bst.add_node(15)               

bst.print_in_order()
print(bst.sortedlist) #check to see it worked

sorted_list = str(bst.sortedlist).translate(str.maketrans(' ', ' ', string.punctuation)) #assign the in-order traversal to a variable that can be sent to LinkedList. Use the translate and makestrans methods of string to clear out the punctiation from the list.
print(sorted_list)

sorted_linked = LinkedList(sorted_list[0]) #create a new instance of LinkedList class, using the index 0 from our list as the   
                                            #head_node value
for item in sorted_list[1:]: #iterate through the list from the first index on since i0 was already added.
    sorted_linked.append_node(item) #append each item as a new node in the linked list, now ordered.

print(sorted_linked) 