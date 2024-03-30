class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # initialize adjacency list for each course
        graph = {i: [] for i in range(numCourses)} 
        # add to each node it's prerequisites
        for i, j in prerequisites:
            graph[i].append(j)

        # visited set to detect loops
        visited = set()

        def dfs(node):
            
            # if loop is detected, then we return False
            if node in visited:
                return False
            
            # if course can be completed return True
            if graph[node] == []:
                return True
            
            # add node the visited set
            visited.add(node)

            # run dfs in each of the prerequisites
            # if one fails, we return false immediately
            for prerequisite in graph[node]:
                if not dfs(prerequisite):
                    return False
            
            # remove node from visited and change the adjacency list
            # since it can be completed and return True
            visited.remove(node)
            graph[node] = []
            return True
        
        # for loop for each node, since the graph can have
        # disconnected nodes
        for course in range(numCourses):
            if not dfs(graph[course]):
                return False
        
        # if all courses can be taken, then return True
        return True


