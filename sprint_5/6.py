class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def print_range(node, l, r):
    if node is None:
        return
    if node.value < l:
        print_range(node.right, l, r)
        if node.value >= l:
            print(node.value)
    elif node.value >= l:
        print_range(node.left, l, r)
        if node.value <= r:
            print(node.value)
        if node.value <= r:
            print_range(node.right, l, r)
