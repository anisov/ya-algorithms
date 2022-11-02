class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def insert(root, key):
    if root.value <= key:
        if root.right is None:
            root.right = Node(None, None, key)
        else:
            insert(root.right, key)
    if root.value > key:
        if root.left is None:
            root.left = Node(None, None, key)
        else:
            insert(root.left, key)
    return root
