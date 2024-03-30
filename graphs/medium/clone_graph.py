import collections

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        copy_hashmap = {}

        def clone_dfs(node):

            # if node already copied
            # return it's copied version
            if node in copy_hashmap:
                return copy_hashmap[node]
            
            # if not create copied node
            copy_node = Node(node.val)

            # add copied node to hashmap
            copy_hashmap[node] = copy_node

            # for each of it's neighbors create a copy node
            # and add them to current copied node neighbors
            for ngh in node.neighbors:
                copy_node.neighbors.append(clone_dfs(ngh))

            # return the copied node with the value and 
            # with it's neighbors
            return copy_node
        
        return clone_dfs(node)

            