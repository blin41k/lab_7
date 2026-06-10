import unittest


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


class TestTreeAnagram(unittest.TestCase):
    def test_symmetric_tree(self):
        root = Node(1)
        root.left = Node(2, Node(3), Node(4))
        root.right = Node(2, Node(4), Node(3))
        self.assertTrue(solution(root))

    def test_not_symmetric_tree(self):
        root = Node(1)
        root.left = Node(2, None, Node(3))
        root.right = Node(2, None, Node(3))
        self.assertFalse(solution(root))

    def test_empty_tree(self):
        self.assertTrue(solution(None))


if __name__ == "__main__":
    unittest.main()