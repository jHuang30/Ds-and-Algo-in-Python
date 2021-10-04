# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, pre_sum, dic = 0, 0, {}
        dic[0] = 1
        for num in nums:
            pre_sum += num
            if pre_sum - k in dic:
                res += dic[pre_sum - k]
            dic[pre_sum] = dic.get(pre_sum, 0) + 1
                
        return res
