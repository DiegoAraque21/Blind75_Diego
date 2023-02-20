"""

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


Example:

Input: root = [3,1,4,null,2], k = 1
Output: 1

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # counter to compare with k
        deletes = 0
        # stack for the iterative DFS
        stack = []
        # current node we are at
        curr_node = root

        # while the tree has not been fully traversed and the currentNode is not None
        while curr_node or stack:
            # while there are lements to the left
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            
            # get the element that was popped
            curr_node = stack.pop()
            deletes += 1

            # if the counter of deletions is the same as k, then we return
            if deletes == k:
                return curr_node.val

            # if it wasn't the correct index, change to the right subtree of current
            curr_node = curr_node.right
