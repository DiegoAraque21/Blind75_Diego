class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # initial grid values
        ROWS, COLS = len(heights), len(heights[0])

        # set to keep track of nodes that reach pacific ocean
        # antoher one o=for the atlantic ocean
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            # check if it's already in atlantic or pacific set
            # if it's out of bounds
            # ir if it cannot pass to the nest cell
            if ((r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            
            # add node to corresponding atlantic or pacific set
            visited.add((r,c))

            # define boundaries, and run dfs for the children
            boundaries = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for bound in boundaries:
                dfs(bound[0], bound[1], visited, heights[r][c])
            


        # traverse only for the first column, nodes reach the pacific ocean
        # traverse the last column, nodes reach the atlantic ocean
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # traverse only for the first row, nodes reach the pacific ocean
        # traverse the last row, nodes reach the atlantic ocean
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        # traverse all the positions in the matrix
        #  if the position being traversed is on both atlantic
        #  and pacific sets, then they are added to our result
        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        
        return result