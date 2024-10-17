from avl import *

def tree_sum(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return root.key

    return tree_sum(root.left) + root.key + tree_sum(root.right)


# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1, 100]

for key in keys:
    root = insert(root, key)

print(f"Sum is: {tree_sum(root)}")
print(f"Expected sum is: {sum(keys)}")
