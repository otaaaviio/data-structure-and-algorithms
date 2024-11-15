class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return ' -> '.join(result)

    def insertAtBegin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    def removeFirstNode(self):
        if self.head is None:
            return None
        
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
        return removed_value
    
    def removeLastNode(self):
        if self.tail is None:
            return None
        
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return removed_value
        

# tests

# Create a doubly linked list
# dll = DoublyLinkedList()
# print("Initial List (empty):", dll)  # expected: ""

# Test insertion at the beginning
# dll.insertAtBegin(10)
# print("After inserting 10 at the beginning:", dll)  # expected: "10"

# dll.insertAtBegin(20)
# print("After inserting 20 at the beginning:", dll)  # expected: "20 -> 10"

# dll.insertAtBegin(30)
# print("After inserting 30 at the beginning:", dll)  # expected: "30 -> 20 -> 10"

# Test insertion at the end
# dll.insertAtEnd(40)
# print("After inserting 40 at the end:", dll)  # expected: "30 -> 20 -> 10 -> 40"

# dll.insertAtEnd(50)
# print("After inserting 50 at the end:", dll)  # expected: "30 -> 20 -> 10 -> 40 -> 50"

# Test removal of the first node
# removed = dll.removeFirstNode()
# print(f"After removing the first node ({removed}):", dll)  # expected: "20 -> 10 -> 40 -> 50"

# Test removal of the last node
# removed = dll.removeLastNode()
# print(f"After removing the last node ({removed}):", dll)  # expected: "20 -> 10 -> 40"

# Test removal until the list is empty
# dll.removeFirstNode()
# dll.removeFirstNode()
# dll.removeFirstNode()
# print("After removing all nodes:", dll)  # expected: ""

# tests