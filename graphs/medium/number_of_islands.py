import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # empty grid
        if not grid:
            return 0
        
        # initalize important values
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # bfs to traverse graph
        def bfs(row, col):
            # bfs works with a queue
            queue = collections.deque()
            # add node to visited set
            visited.add((row, col))
            # add curr node to the queue to start the bfs
            queue.append((row, col))

            # while queue is not empty
            while queue:
                # get the first element out
                r, c = queue.popleft()
                # get boundarie nodes
                boundaries = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]

                # for each of the nodes check if it has an adjacent 1
                # check out of bounds
                for br, bc in boundaries:

                    if (br in range(ROWS) and
                        bc in range(COLS) and
                        grid[br][bc] == "1" and
                        (br, bc) not in visited):

                        queue.append((br, bc))
                        visited.add((br, bc))

        # for loops for each node in grid
        for row in range(ROWS):
            for col in range(COLS):
                # if node is a 1 and has not been visited yet
                # we have found ourselves a new island
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands