class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def search(self, root, value):
        pass

    def insert(self, hhh, data):
        if self.root is None:
            self.root = TreeNode(data)
            return
        if data > self.root.data:
            self.insert(self.root.right, data)
        elif data < self.root.data:
            self.insert(self.root.left, data)


    def delete(self, root: TreeNode, data):
        pass

    def in_order(self):
        pass

o = BinaryTree()
o.insert(None, 8)
o.insert(8, 9)
print(o.root.data)