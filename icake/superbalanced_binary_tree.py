"""
Write a function to see if a binary tree is "superbalanced"

A tree is "superbalanced" if the difference between the depths of any two leaf
nodes is no greater than one.
"""
class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        # if left and/or right aren't specified,
        # they get a default value of None
        self.value = value
        self.left  = left
        self.right = right

def is_super_balanced(binary_tree):
    max_depth = float('inf') 
    min_depth = 0
    def get_leaf_depth(node, depth=0):
        """update min_depth and max_depth if node is leaf"""
        if node.left == None and node.right == None:
            # This is a leaf
            if depth > max_depth:
                max_depth = depth
            if depth < min_depth:
                min_depth = depth
        else:
            if node.left is not None:
                get_leaf_depth(node.left, depth + 1)
            if node.right is not None:
                get_leaf_depth(node.right, depth + 1)

    if binary_tree.right is not None:
        get_leaf_depth(binary_tree.right, 1)
    if binary_tree.left is not None:
        get_leaf_depth(binary_tree.left, 1)

    return max_depth - min_depth <= 1
            
