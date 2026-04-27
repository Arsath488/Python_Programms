class Solution:
    def totalNQueens(self, n):
        # Tracking occupied columns and diagonals
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        self.count = 0
        
        def backtrack(r):
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                # Check if this position is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # "Place" the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Move to the next row
                backtrack(r + 1)
                
                # "Remove" the queen (Backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        backtrack(0)
        return self.count
