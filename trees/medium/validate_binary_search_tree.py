"""

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example:

Input: root = [2,1,3]
Output: true

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.isSubtreeBST(root, float("-inf"), float("inf"))
        
    def isSubtreeBST(self, node, left, right):
        # if node exists
        if node:
            # check values are right, if not return False
            if node.val <= left or node.val >= right:
                return False
            # recursive step
            left_tree = self.isSubtreeBST(node.left, left, node.val)
            right_tree = self.isSubtreeBST(node.right, node.val, right)

            return left_tree and right_tree

        return True