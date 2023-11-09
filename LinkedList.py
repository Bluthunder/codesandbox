class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    '''
    This creates a LinkedList with single node
    '''
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1






# Tests 
new_linked_list = LinkedList(10)
print(new_linked_list.head.value, new_linked_list.length)

