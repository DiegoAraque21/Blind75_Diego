class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        grid = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # if same character, look diagonaly
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i+1][j+1]
                # max between down and up
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])

        return grid[0][0] 