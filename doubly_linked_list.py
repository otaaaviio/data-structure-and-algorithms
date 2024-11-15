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
        

# # Testes

# # Criação de uma lista vazia
# dll = DoublyLinkedList()
# print("Lista inicial (vazia):", dll)  # Esperado: ""

# # Teste de inserção no início
# dll.insertAtBegin(10)
# print("Após inserir 10 no início:", dll)  # Esperado: "10"

# dll.insertAtBegin(20)
# print("Após inserir 20 no início:", dll)  # Esperado: "20 -> 10"

# dll.insertAtBegin(30)
# print("Após inserir 30 no início:", dll)  # Esperado: "30 -> 20 -> 10"

# # Teste de inserção no final
# dll.insertAtEnd(40)
# print("Após inserir 40 no final:", dll)  # Esperado: "30 -> 20 -> 10 -> 40"

# dll.insertAtEnd(50)
# print("Após inserir 50 no final:", dll)  # Esperado: "30 -> 20 -> 10 -> 40 -> 50"

# # Teste de remoção do primeiro nó
# removed = dll.removeFirstNode()
# print(f"Ao remover o primeiro nó ({removed}):", dll)  # Esperado: "20 -> 10 -> 40 -> 50"

# # Teste de remoção do último nó
# removed = dll.removeLastNode()
# print(f"Ao remover o último nó ({removed}):", dll)  # Esperado: "20 -> 10 -> 40"

# # Teste de remoção até esvaziar a lista
# dll.removeFirstNode()
# dll.removeFirstNode()
# dll.removeFirstNode()
# print("Após remover todos os nós:", dll)  # Esperado: ""

# # Teste de remoção de uma lista vazia
# removed = dll.removeFirstNode()
# print("Remover de lista vazia (primeiro nó):", removed)  # Esperado: None

# removed = dll.removeLastNode()
# print("Remover de lista vazia (último nó):", removed)  # Esperado: None
