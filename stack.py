class Node:
    def __init__(self, value):
        self.value = value
        self.previus = None
        
class Stack:
    def __init__(self):
        self.tail = None
        
    def __str__(self):
        result = []
        current = self.tail
        while current:
            result.append(str(current.value))
            current = current.previus
        return ' <- '.join(result)
    
    def append(self, value):
        new_node = Node(value)
        
        if self.tail is None:
            self.tail = new_node
            return
        
        new_node.previus = self.tail
        self.tail = new_node
    
    def pop(self):
        if self.tail is None:
            return
        
        if self.tail.previus is None:
            self.tail = None
            return
        
        self.tail =self.tail.previus
  
  
# tests
          
# stack = Stack()
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.pop()
# print(stack)

# tests