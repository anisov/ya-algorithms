class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return True

    right_result = solution(root.right)
    left_result = solution(root.left)
    if (
        (root.right and not root.right.value > root.value)
        or (root.left and not root.value > root.left.value)
        or (not right_result or not left_result)
    ):
        return False
    return True
