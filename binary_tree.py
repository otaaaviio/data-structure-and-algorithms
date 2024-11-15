class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, val):
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

    def search(self, val):
        if self.value == val:
            return True
        
        if val < self.value and self.left:
            return self.left.search(val)

        elif val > self.value and self.right:
            return self.right.search(val)

        return False

    def preorder_traversal(self, res=None):
        if res is None:
            res = []

        res.append(self.value)

        if self.left:
            self.left.preorder_traversal(res)
            
        if self.right:
            self.right.preorder_traversal(res)

        return res

    def inorder_traversal(self, res=None):
        if res is None:
            res = []

        if self.left:
            self.left.inorder_traversal(res)

        res.append(self.value)

        if self.right:
            self.right.inorder_traversal(res)

        return res

    def postorder_traversal(self, res=None):
        if res is None:
            res = []

        if self.left:
            self.left.postorder_traversal(res)

        if self.right:
            self.right.postorder_traversal(res)

        res.append(self.value)

        return res
    
    
    def dfs(self, val):
        if self.value: 
            print(self.value)
        if self.value == val:
            return self
        
        if self.left:
            left_found = self.left.dfs(val)
            if left_found:
                return left_found 
            
        if self.right:
            return self.right.dfs(val)
        
        return None


# tests

# root = TreeNode(5)
# root.insert(3)
# root.insert(1)
# root.insert(10)
# root.insert(7)
# root.insert(15)
# print("has 12 in binary tree: ", root.search(12))
# print("has 10 in binary tree: ", root.search(10))
# print("preorder traversal: ", root.preorder_traversal())
# print("inorder traversal: ", root.inorder_traversal())
# print("postorder traversal: ", root.postorder_traversal())
# print("dfs(10): ", root.dfs(10))

# tests
