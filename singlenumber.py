class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            # XOR the current number with the running result
            result ^= num
        return result
