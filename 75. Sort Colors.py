# Given an array nums with n objects colored red, white, or blue, sort them in -place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.


# Example 1:

# Input: nums = [2, 0, 2, 1, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]
# Example 2:

# Input: nums = [2, 0, 1]
# Output: [0, 1, 2]
# Example 3:

# Input: nums = [0]
# Output: [0]
# Example 4:

# Input: nums = [1]
# Output: [1]


# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is 0, 1, or 2.


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        start = i = 0
        end = len(nums) - 1

        while i <= end:
            if nums[i] == 0:
                nums[i] = nums[start]
                nums[start] = 0
                i += 1
                start += 1
            elif nums[i] == 2:
                nums[i] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                i += 1
        return nums
