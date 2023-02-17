"""

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # queue for our bfs
        queue = deque([root])
        # result arr
        result = []
        # BFS
        while queue:
            # level arr
            level_res = []
            for i in range(len(queue)):
                node = queue.popleft()
                # if the node is not null, then add it's children to queue
                # and itself to the level_res
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level_res.append(node.val)
            # add level_res to result
            if len(level_res) > 0:
                result.append(level_res)
        
        return result