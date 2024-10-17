from avl import *

def find_max(root):
    if not root:
        return root

    if not root.right:
        return root

    return find_max(root.right)


# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1, 100]

for key in keys:
    root = insert(root, key)

print(f"Max value: {find_max(root).key}")
