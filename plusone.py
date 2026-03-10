class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Move from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9, it becomes 0 and we continue to the next iteration
            digits[i] = 0
            
        # If we are here, it means all digits were 9 (e.g., [9, 9, 9])
        # We need to prepend a 1 (e.g., [1, 0, 0, 0])
        return [1] + digits
