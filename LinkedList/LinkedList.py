class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    '''
    This creates a LinkedList with single node
    '''
    # def __init__(self,value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

    '''
    Insertion of nodes 
    1. Start of LinkedList - Prepend
    2. Middle of LinkedList - Insert
    3. End of LinkedList - Append
    '''
    # Append

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return -1
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1


# Tests
new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
print(new_linked_list)
new_linked_list.prepend(5)
print(new_linked_list)
new_linked_list.insert(15, -1)
print(new_linked_list)
