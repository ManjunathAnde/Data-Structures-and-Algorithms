# Problem: Top K Frequent Elements
# Date: 17/3/2026

# Approach: HashMap for frequency counting + Bucket Sort
# Time: O(n) - counting pass + filling buckets + inspecting buckets
# Space: O(n) - hashmap and buckets both scale with input

# Mental analogy: Count the number of balls and take note of
# how many balls exist of each color. Then take n boxes
# labeled 1 to n, n being total number of balls of all colors.
# Keep balls of each color in their respective box based on
# frequency. Walk from the highest box downward and collect
# top k colors.

class Solution:
    def topKFrequent(self, nums, k):
        hashmap = {}
        for num in nums:  #Inserting in hashmap with value:frequency
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)] #create n buckets

        for key, value in hashmap.items():  # add elements in buckets based on frequenct
            buckets[value].append(key)

        k_elements = []
        for i in range(len(buckets)-1, -1, -1):  #walk back through buckets and return topk
            if k == 0:
                break
            if not buckets[i]:
                continue
            for num in buckets[i]:
                if len(k_elements) == k:
                    break
                k_elements.append(num)

        return k_elements