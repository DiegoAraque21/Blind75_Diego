"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:

Input: root = [3,9,20,null,null,15,7]
Output: 3

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive. O(n) in space and time
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root:
            temp_root = root.left
            # left
            root.left = self.invertTree(root.right)
            # right
            root.right = self.invertTree(temp_root)

        return root
