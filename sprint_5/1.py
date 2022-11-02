class Node:
    def __init__(self, value, left=None, right=None):
        self.value = int(value)
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return float("-inf")
    max_value = root.value
    right_value = solution(root.right)
    left_value = solution(root.left)
    return max(max_value, right_value, left_value)
