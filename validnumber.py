class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, char in enumerate(s):  
            if char.isdigit():
                seen_digit = True
            
            elif char in "+-":
                # A sign is only valid at the start OR immediately after an 'e/E'
                if i > 0 and s[i-1] not in "eE":
                    return False
            
            elif char in "eE":
                # Exponent is invalid if already seen OR if no digits preceded it
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                # Reset digit flag for the exponent part (e must be followed by digits)
                seen_digit = False 
            
            elif char == ".":
                # Dot is invalid if already seen OR if it appears after an exponent
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            
            else:
                # Any other character (like 'a', 'b', 'abc') is invalid
                return False
        
        # The string is valid only if at least one digit was seen 
        # (and if 'e' was seen, seen_digit was reset and must be found again)
        return seen_digit
