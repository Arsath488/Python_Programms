class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows, cols = len(s), len(p)
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, or a*b*c* matching an empty string
        for j in range(2, cols + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if p[j-1] == '*':
                    # Case 1: Match 0 of the preceding element
                    res = dp[i][j-2]
                    # Case 2: Match 1 or more (if preceding element matches)
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        res = res or dp[i-1][j]
                    dp[i][j] = res
                else:
                    # Direct match or '.'
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
        
        return dp[rows][cols]
