# 69197186
# Для удаления узла, необходимо сначала найти данный узел с его родителем
# в дереве, для этого используется функция fined_node, после того как
# необходимый узел с родителем был найден, необходимо найти узел на который
# его можно заменить, для этого используются функции find_right_min и
# find_left_min. Затем когда нужный узел для замены будет найден, происходит
# переназначение детей удаляемого узла и изменяется ссылка у родителя на новый
# узел. Так же учтены случаи, когда удаляемым узлом является корень дерева,
# а так же когда у удаляемого узла нет детей или нет одного из детей или
# необходимого узла вообще нет в дереве.
# Временная сложность: O(h), где h - высота дерева. В худшем случае: O(n).
# Пространственная сложность: O(h), где h - высота дерева


def fined_node(root, key):
    parent_node = None
    while root is not None:
        if root.value == key:
            return root, parent_node
        parent_node = root
        if root.right is None or root.left is None:
            root = root.left or root.right
            continue
        root = root.right if key > root.value else root.left
    return None, None


def find_right_min(node, parent):
    if node.left:
        return find_right_min(node.left, node)
    else:
        return node, parent


def find_left_min(node, parent):
    if node.right:
        return find_left_min(node.right, node)
    else:
        return node, parent


def remove(root, key):
    node, parent_node = fined_node(root, key)
    if not node:
        return root
    if node.right is None and node.left is None:
        min_node = None
    else:
        min_node, min_parent_node = (
            find_right_min(node.right, node)
            if node.right
            else find_left_min(node.left, node)
        )
        if min_node == min_parent_node.left:
            min_parent_node.left = None
        else:
            min_parent_node.right = None
    if min_node:
        min_node.right = min_node.right or node.right
        min_node.left = min_node.left or node.left
    if not parent_node:
        root = min_node
    elif parent_node.right == node:
        parent_node.right = min_node
    else:
        parent_node.left = min_node
    return root
