
## main.py

"""
HW04 — Forest Watchtower (Balanced Tree Check)

Implement TreeNode and is_balanced(root) to check if a binary tree is height-balanced.
"""


class TreeNode:
    """
    Simple binary tree node: value, left, right.
    """

    def __init__(self, value, left=None, right=None):
        # TODO: store the given fields on the instance
        # Example:
        # self.value = value
        # self.left = left
        # self.right = right
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Return True if the binary tree rooted at `root` is height-balanced.

    Empty tree (root is None) is considered balanced.
    """
    # TODO (8 Steps of Coding, minimal prompts):
    # - Design a helper that checks balance and height in one traversal.
    # - Implement the recursive logic.
    # - Test on small examples (empty tree, single node, skewed tree).
    
    def check_balance(node):
        # Helper function returns (is_balanced, height)
        if node is None:
            return True, 0
        
        left_balanced, left_height = check_balance(node.left)
        if not left_balanced:
            return False, 0
        
        right_balanced, right_height = check_balance(node.right)
        if not right_balanced:
            return False, 0
        
        height_diff = abs(left_height - right_height)
        is_balanced_node = height_diff <= 1
        height = max(left_height, right_height) + 1
        
        return is_balanced_node, height
    
    balanced, _ = check_balance(root)
    return balanced


if __name__ == "__main__":
    # Optional: quick manual tree
    #   1
    #  / \
    # 2   3
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)
    print(is_balanced(root))
