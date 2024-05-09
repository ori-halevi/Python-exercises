class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def search(self, value):
        return self.search_rec(self.root, value)

    def search_rec(self, root, value) -> object:
        if not root:
            return False
        elif value == root.data:
            return True
        elif root.data > value:
            return self.search_rec(root.left, value)
        elif root.data < value:
            return self.search_rec(root.right, value)

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
o.insert(18)
o.insert(3)
# print(o.root.right.data)
print()
print(o.search(3))