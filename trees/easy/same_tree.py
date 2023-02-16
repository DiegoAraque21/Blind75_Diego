"""

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Explanation:

Input: p = [1,2,3], q = [1,2,3]
Output: true

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # both are None
        if not p and not q:
            return True
        # not equal
        if (not p and q )or (p and not q) or (p.val != q.val):
            return False
        
        # recursive step. Traverse through the left and right side of each tree
        res1 =  self.isSameTree(p.left, q.left)
        res2 = self.isSameTree(p.right, q.right)

        # if both are true, the trees match
        if res1 and res2:
            return True
        else:
            return False
