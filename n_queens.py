class Solution:
    def solveNQueens(self, n):
        res = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        def backtrack(r):
            if r == n:
                # Format board into strings
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place Queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # Move to next row
                backtrack(r + 1)
                
                # Remove Queen (Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return res
