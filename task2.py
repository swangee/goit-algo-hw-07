from avl import *

def find_min(root):
    if not root:
        return root

    if not root.left:
        return root

    return find_min(root.left)


# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1, 100]

for key in keys:
    root = insert(root, key)

print(f"Min value: {find_min(root).key}")
