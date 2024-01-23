# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # result value for the max path
        res = [root.val]

        def path_calc(root):

            # null means we don't return a value for path
            if not root:
                return 0
            
            # get value of the left tree, max and also for right
            left_max = path_calc(root.left)
            right_max = path_calc(root.right)

            # if it's a negative numebr transform the max to 0, since we are not going to use it
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # do the sum of the entire path
            res[0] = max(res[0], root.val + left_max + right_max)

            # return the sum of the parent node and the max of right or left node
            return  root.val + max(left_max, right_max)
        
        # recursive call
        path_calc(root)

        return res[0]

            
        