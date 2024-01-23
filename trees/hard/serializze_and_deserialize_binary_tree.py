# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # result of the serialiazation to a string
        self.res = ""

        def dfs(node):

            # if we are on a null node, we append N to the string with it's separator
            if not node:    
                res_2 = self.res + "|" + "N"
                self.res = res_2
                return 

            # if not we append the number as a string with the separator
            res_2 = self.res + "|" + str(node.val)
            self.res = res_2

            # recursive call for left and right
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # return the serialization
        return self.res[1:]
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # split the nodes with the | separator already defined in our structure
        nodes = data.split("|")

        # define global variable for class for the dfs to acces values easier
        self.i = 0

        def dfs():
            # if we are on a null node, advance pointer and don't create any nodes
            if nodes[self.i] == "N":
                self.i += 1
                return None
            
            # create the tree node for the corresponding number
            node_tree = TreeNode(int(nodes[self.i]))

            # increase pointer for next expansions
            self.i += 1

            # assign children with recursive call
            node_tree.left = dfs()
            node_tree.right = dfs()

            # return the tree
            return node_tree
        
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))