# DCP 116
# Generate an arbitrarily large binary tree in O(1)
# Jane Street
import random

class Node():
    
    def __init__(self):
        self.left = None
        self.right = None

def generate():
    x = random.randint(0, 1)
    if x == 0:
        return Node()
    if x == 1:
        n = Node()
        n.left = generate()
        n.right = generate()
        return n

def dfs(root):
    
    if root.right is None and root.left is None:
        return 1
    if root.right is None:
        return dfs(root.left) + 1
    if root.left is None:
        return dfs(root.right) + 1
    return dfs(root.right) + dfs(root.left) + 1

x = generate()         
print dfs(x)
