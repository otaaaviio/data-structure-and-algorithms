class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(self.value, end=' ')
      if self.right:
         self.right.PrintTree()
        
    def insert(self, val):
        if self.value:
            if val < self.value:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.value:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.value = val
            
    def search(self, val):
        if self.value == val:
            return True
        
        if val < self.value and self.left:
            self.left.search(val)
        elif val > self.value and self.right:
            self.right.search(val)
        
        return False
  
# tests          

# root = TreeNode(1)
# root.insert(7)
# root.insert(3)
# root.insert(2)
# root.insert(5)
# root.insert(4)
# root.PrintTree()
# print('')
# print('has 1 in binary tree: ', root.search(1))
# print('has 10 in binary tree: ', root.search(10))

# tests          