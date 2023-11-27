class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def remove_duplicates(self):
        if self.head is None:
            return 
        node_values = set()
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next is not None:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node



newLinkedList = LinkedList()
newLinkedList.append(1)
newLinkedList.append(2)
newLinkedList.append(3)
newLinkedList.append(4)
newLinkedList.append(5)
print(newLinkedList)
print(newLinkedList.find_middle().value)
