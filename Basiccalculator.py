class BasicCalculator:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        sign = 1
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        return res + sign * num

class Solution(BasicCalculator):
    pass
