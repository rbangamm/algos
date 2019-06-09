def prune(node):
    if node.left is None and node.right is None:
        return node
    if node.left is not None and node.right is not None:
        node.left = prune(node.left)
        node.right = prune(node.right)
        return node
    if node.right is None:
        return prune(node.left)
    if node.left is None:
        return prune(node.right)

class Node():

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)
    return

n = Node(0, 
        Node(1, 
            Node(3, 
                None, 
                Node(5,
                    None,
                    None)), 
            None), 
        Node(2, 
            None, 
            Node(4, 
                Node(6, 
                    None, 
                    None), 
                Node(7, 
                    None, 
                    None))))
in_order(n)
print("\n")
n = prune(n)
in_order(n)
