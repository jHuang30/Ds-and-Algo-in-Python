
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_idx(left):
            l, r = 0, len(nums)
            
            while l < r:
                mid = (r + l) // 2
                if nums[mid] > target or (left and nums[mid] == target):
                    r = mid
                else:
                    l = mid + 1
            return l
        
        res = []
        left = find_idx(True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        res.append(left)
        res.append(find_idx(False) - 1)
        return res