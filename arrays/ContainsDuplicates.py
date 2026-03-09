# Problem: Contains Duplicate
# Date: 9/3/2026

# Approach: HashSet
# Time: O(n) - one complete search through array
# Space: O(n) - set stores up to n elements

# Mental analogy: picking up colored balls, check if color
# already in box(set) before dropping it in(return True). If it is not there, return False 

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False