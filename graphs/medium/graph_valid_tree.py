# time complexity normal dfs O(v+e) which can be simplified to O(n), 
# n being all nodes and vertices in the graph
class Solution:
    def validTree(self, n, edges):

        if not n:
            return True
        
        # create adjacency list
        graph = {i: [] for i in range(n)}

        # add neighbors to the adj list
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        # visited set, usefull to check if all nodes are connected
        visited = set()

        # dfs function to check cycle
        def dfs(curr_node, prev_node):

            # cycle detected
            if curr_node in visited:
               return False
           
            # add node to visited list
            visited.add(curr_node)

            # search on each neighbor
            for neighbor in graph[curr_node]:
                # if it isn't the previous node, search it
               if neighbor != prev_node:
                    # cycle found? return False    
                   if not dfs(neighbor, curr_node):
                       return False
            return True
        
        # if no cycle was found, and every node is connected
        if dfs(0,-1) and n == len(visited):
            return True
        else:
            return False


# creative solution with union find. Time complexity will be 0(n + m), n only being the size of the edges array
# and m being the amount of nodes in the graph
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
#         parents = [i for i in range(n)]
#         rank = [1] * n

#         def find(node):
            
#             curr = node
#             while curr != parents[curr]:
#                 # path compression
#                 parents[curr] = parents[parents[curr]]
#                 curr = parents[curr] 


#             return parents[curr]
            
        
#         def union(n1, n2):
#             # find parents of the nodes
#             node1, node2 = find(n1), find(n2)

#             # found cycle
#             if node1 == node2:
#                 return False

#             if rank[node1] >= rank[node2]:
#                 parents[node2] = node1
#                 rank[node1] += 1
#             else:
#                 parents[node1] = node2
#                 rank[node2] += 1
            
#             return True
            
        
#         for node1, node2 in edges:
#             if not union(node1, node2):
#                 return False
        
#         parent = parents[0]

#         for p in parents:
#             if p != parent:
#                 return False
                
#         return True