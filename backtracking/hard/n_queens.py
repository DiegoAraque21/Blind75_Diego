class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        # a queen must be in a unique column, positive
        # diagonal, negative diagonal and row. To not kill another
        # queen
        col, pos_diag, neg_diag = set(), set(), set()

        res = []
        # n*n board, initialize with only dots
        board = [["."] * n for _ in range(n)]

        # recursive function
        def backtrack(r):
            # once r is the same as n, we place a queen
            # in every row and we are finished
            if r == n:
                # change format of the board, and add it
                # to the result array
                copy_board = ["".join(row) for row in board]
                res.append(copy_board)
                return
            
            # for each column left
            for c in range(n):
                # check if the column, or diagonals have been ocupied
                if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                # if not add everithing to their respective sets
                # and make the dot a queen
                col.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = "Q"

                # recursive step for the next row
                backtrack(r+1)

                # cleanup, since we are not using that data anymore
                col.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = "."
       
        backtrack(0)

        return res