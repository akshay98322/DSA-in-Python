class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.data == value:
        return root
    if value < root.data:
        return search(root.left, value)
    return search(root.right, value)

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=' ')
        in_order_traversal(root.right)

root = insert(None, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 1)
root = insert(root, 5)
in_order_traversal(root)

if search(root, 700):
    print("\nValue found in the BST.")
else:
    print("\nValue not found in the BST.")

