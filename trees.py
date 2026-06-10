class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_mirror(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    if left.value != right.value:
        return False

    return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)


def solution(root):
    if root is None:
        return True

    return is_mirror(root.left, root.right)