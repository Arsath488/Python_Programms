class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() # 1. Remove leading whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # 2. Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        res = 0
        # 3. Process digits
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply sign
        res *= sign
        
        # 4. Handle rounding (32-bit limits)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
