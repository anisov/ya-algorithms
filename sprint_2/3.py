class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node(head, index):
    node = head
    for i in range(index):
        node = node.next_item
    return node


def solution(node, idx):
    if idx == 0:
        head = node.next_item
        return head
    prev_node = get_node(node, idx - 1)
    next_node = get_node(node, idx + 1)
    prev_node.next_item = next_node
    return node
