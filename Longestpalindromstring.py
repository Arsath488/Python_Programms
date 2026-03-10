class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length (center is a character like 'aba')
            len1 = expandAroundCenter(i, i)
            # Case 2: Even length (center is between characters like 'abba')
            len2 = expandAroundCenter(i, i + 1)
            
            max_len = max(len1, len2)
            
            # If a new longest palindrome is found, update start and end
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]
