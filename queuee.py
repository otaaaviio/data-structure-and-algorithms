class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)

    def put(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            return

        self.head = self.head.next


# tests

# queue = Queue()
# queue.put(1)
# queue.put(2)
# queue.put(3)
# queue.put(4)
# queue.pop()
# queue.pop()
# print(queue)

# tests
