class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # grid to store values of how much paths to get there
        grid = [[0 for _ in range(n)]] * m

        # complexity O(m*n)
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                # if we are on the last row, then all of the
                # unique path are 1
                if i == m - 1:
                    grid[i][j] = 1
                # if we are on the last col, then all of the
                # unqiue paths are also 1
                elif j == n-1:
                    grid[i][j] = 1
                # if we are on another part of the grid,
                # then the unique paths are down + right
                else:
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]
        return grid[0][0]