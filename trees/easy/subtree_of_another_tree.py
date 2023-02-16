"""

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        # subRoot = None. Then it will be a subtree of every single possible tree
        if not subRoot:
            return True
        # if root is none, and we also know that subRoot isn't, then we return False
        if not root:
            return False
        
        # if the tree is the same
        if self.sameTree(root, subRoot):
            return True
        
        # check left and right of that node. Recursive step
        sub_tree_left = self.isSubtree(root.left, subRoot)
        sub_tree_right = self.isSubtree(root.right, subRoot)

        # if one of them is true, it means subroot is a subtree of root
        if sub_tree_left or sub_tree_right:
            return True
        else:
            return False
        
    
    def sameTree(self, tree1, tree2):
        # both are None
        if not tree1 and not tree2:
            return True
        # not equal
        if ((not tree1 and tree2) or (tree1 and not tree2)) or tree1.val != tree2.val:
            return False
        
        # check if the left and right nodes are the same, recursive step
        node1 = self.sameTree(tree1.left, tree2.left)
        node2 = self.sameTree(tree1.right, tree2.right)

        # if both are the same return true
        if node1 and node2:
            return True
        else:
            return False