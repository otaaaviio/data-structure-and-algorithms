class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        values = []
        
        while self:
            values.append(str(self.value))
            self = self.next
        string = ' -> '.join(values)
        return string


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return ' -> '.join(result)
    
    def insertAtBeginArray(self, values):
        for value in values:
            self.insertAtBegin(value)

    def insertAtBegin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, value, index):
        if index == 0:
            return self.insertAtBegin(value)
        
        position = 0
        current_node = self.head

        while position + 1 != index and current_node != None:
            position += 1
            current_node = current_node.next

        if current_node is None:
            print('index not present')
            return
        
        new_node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node
    
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node
        
    def updateNode(self, new_value, index):
        position = 0
        current_node = self.head
        
        if position == index:
            current_node.value = new_value
            
        while current_node != None and position != index:
            position += 1
            current_node = current_node.next
        
        if current_node is None:
            print('index not present')
            return
        current_node.value = new_value
        
    def removeFirstNode(self):
        if self.head is None:
            return
        
        self.head = self.head.next
    
    def removeLastNode(self):
        if self.head is None:
            return
        
        current = self.head
        while current.next and current.next.next:
            current = current.next
        
        current.next = None
        
    def removeAtIndex(self, index):
        if self.head is None:
            return

        if index == 0:
            self.removeFirstNode()
            return
        
        position = 0
        current = self.head
        while position + 1 != index and current.next != None:
            current = current.next
            position += 1
            
        if current.next == None:
            print('index not present')
            return
            
        current.next = current.next.next
        

# tests

# linked_list = LinkedList()
# linked_list.insertAtBegin(1)
# linked_list.insertAtEnd(3)
# linked_list.insertAtIndex(2, 1)

# print('expect: 1 -> 2 -> 3')
# print(linked_list)

# linked_list.updateNode(4, 1)

# print('expect: 1 -> 4 -> 3')
# print(linked_list)

# linked_list.removeFirstNode()
# linked_list.removeLastNode()
# linked_list.removeAtIndex(0)

# print('expect: 4')
# print(linked_list)

# tests