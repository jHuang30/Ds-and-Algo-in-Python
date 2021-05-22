# Given an array nums of integers, you can perform operations on the array.

# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

# You start with 0 points. Return the maximum number of points you can earn by applying such operations.


# Example 1:

# Input: nums = [3, 4, 2]
# Output: 6
# Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points.
# 6 total points are earned.
# Example 2:

# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.


# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = [0] * 10001
        for num in nums:
            arr[num] += num
        take_prev, not_take_prev = 0, 0
        for num in arr:
            take_current = not_take_prev + num
            not_take_current = max(take_prev, not_take_prev)
            take_prev = take_current
            not_take_prev = not_take_current
        return max(take_prev, not_take_prev)


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = [0] * 10001
        for num in nums:
            arr[num] += num
        take_prev_one, take_prev_two = 0, 0
        for num in arr:
            temp = take_prev_one
            take_prev_one = max(take_prev_two + num, take_prev_one)
            take_prev_two = temp
        return take_prev_one
