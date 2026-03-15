# Problem: Two Sum
# Date: 15/3/2026

# Approach: HashMap to store values and indices
# Time: O(n) - one pass through array
# Space: O(n) - hashmap stores up to n elements

# Mental Analogy: Let's say we have a shoe pair of size 9 (target). We have a collection of 
# different shoes and we need to find two shoes that add up to size 9.
# We pick one shoe, subtract it from 9 to find exactly what the other shoe should look like.
# If that missing shoe is already in our box (hashmap), we found our pair.
# Otherwise, we drop the current shoe in the box and keep searching.

class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in map:
                return (map[difference], i)
            map[nums[i]] = i