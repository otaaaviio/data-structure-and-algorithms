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

# tree = TreeNode(1)
# tree.insert(7)
# tree.insert(3)
# tree.insert(2)
# tree.insert(5)
# tree.insert(4)
# tree.PrintTree()
# print(tree.search(1))
# print(tree.search(10))

# tests          