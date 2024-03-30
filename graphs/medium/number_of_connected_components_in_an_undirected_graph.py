class Solution:
    def countComponents(self, n, edges):
        # at the beginning every node is it's own parent
        # we initialize with n components
        parents = [i for i in range(n)]

        # every single one of the nodes at the beginning only have
        # a rank 1
        rank = [1] * n
        
        # function to find node
        def find(node):
            # temp variable
            res = node

            # while loop to find the parent of current node
            while res != parents[res]:
                # path compression, it can work if we don't use this line. 
                # But we avoid linked list with it. If a node has multiple
                # connections, we save a lot of time
                parents[res] = parents[parents[res]]
                # re-assign curr_node
                res = parents[res]

            return res  

        # unites two nodes, to re-assign parent
        def bind(node1, node2):
            
            # find both nodes parents
            parent1, parent2 = find(node1), find(node2)

            # if same parent, they are already connected, we just return 0
            # no union made
            if parent1 == parent2:
                return 0
            
            # if not, then we check which parent has more children
            # we don't replicate the same graph in order for
            # the time complexity to decrease.
            if rank[parent2] > rank[parent1]:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]

            # return 1 because we made a union
            return 1
        
        # for each one of the edges, we bind them
        # at the end we return count. It decreases everytime a union
        # is made
        count = n
        for n1, n2 in edges:
            count -= bind(n1, n2)

        return count
