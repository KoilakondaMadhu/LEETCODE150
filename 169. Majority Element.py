
# Solved
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 class Solution:
    def majorityElement(self, nums):
        nums.sort()  # Step 1: Sort the array in non-decreasing order
        n = len(nums) // 2  # Step 2: Calculate the index of the middle element
        return nums[n]  # Step 3: Return the element at the middle index (assumed to be the majority element)


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?
# Seen this question in a real interview before?
# 1/4
# Yes
# No
