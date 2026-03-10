class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        last_non_zero = 0
        
        for current in range(len(nums)):
            if nums[current] != 0:
                # Swap the non-zero element to the front
                nums[last_non_zero], nums[current] = nums[current], nums[last_non_zero]
                last_non_zero += 1
