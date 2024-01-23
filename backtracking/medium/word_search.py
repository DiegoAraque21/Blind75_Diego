class Solution(object):

    def dfs(self, row, column, i, word, board, path):
        if i == len(word):
            return True
        if (row < 0 or column < 0 or 
            row >= len(board) or column >= len(board[0]) or 
            word[i] != board[row][column] or 
            (row, column) in path):
            return False
        print(row, column, word, board[row][column], word[i])
        path.add((row, column))
        res = (self.dfs(row+1, column, i+1, word, board, path) or
               self.dfs(row - 1, column, i+1, word, board, path) or
               self.dfs(row, column + 1, i+1, word, board, path) or
               self.dfs(row, column - 1, i+1, word, board, path))
        path.remove((row, column))
        return res

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        path = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(r,c,0,word,board,path):
                    return True
                
        return False