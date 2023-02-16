"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:

Input: root = [3,9,20,null,null,15,7]
            3
    9               20
                15      7
 
Output: 3

"""


# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursion DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if the node is null, return 0 as it's length
        if not root:
            return 0

        # else calculate the depth of their right and left recursively
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# iterative BFS
# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         # if the node is null, return 0 as it's length
#         if not root:
#             return 0

#         level = 0
#         queue = deque([root])

#         # while the que is not emptty
#         while queue:
#             # get every child, and eliminate nodes from the last level
#             for _ in range(len(queue)):
#                 node = queue.popleft()

#                 if node.right:
#                     queue.append(node.right)
#                 if node.left:
#                     queue.append(node.left)

#             # increase level
#             level += 1
#         # return current level
#         return level
        

# iterative DFS
# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         # if the node is null, return 0 as it's length
#         if not root:
#             return 0

#         depth_result = 1
#         stack = [[root, 1]]

#         while stack:
#             # get every child from every node in the stack
#             node, depth = stack.pop()

#             if node:
#                 depth_result = max(depth_result, depth)
#                 stack.append([node.right, depth + 1])
#                 stack.append([node.left , depth + 1])

#         return depth_result
            


            