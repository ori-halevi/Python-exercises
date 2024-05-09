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

    def insert(self, data):
        self.root = self.insert_rec(self.root, data)

    def insert_rec(self, root, data) -> TreeNode:
        if root is None:
            return TreeNode(data)
        elif data > root.data:
            root.right = self.insert_rec(root.right, data)
        elif data < root.data:
            root.left = self.insert_rec(root.left, data)
        return root

    def delete(self, root: TreeNode, data):
        pass

    def in_order(self):
        pass

o = BinaryTree()
o.insert(9)
o.insert(11)
print(o.root.right.data)
print()
