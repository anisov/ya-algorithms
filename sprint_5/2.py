class Node:
    def __init__(self, value, left=None, right=None):
        self.value = int(value)
        self.right = right
        self.left = left


def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def solution(root):
    if root is None:
        return True
    right_height = get_height(root.right)
    left_height = get_height(root.left)
    right_tree_correct = solution(root.right)
    left_tree_correct = solution(root.left)
    if (
        abs(right_height - left_height) > 1
        or not right_tree_correct
        or not left_tree_correct
    ):
        return False
    return True
