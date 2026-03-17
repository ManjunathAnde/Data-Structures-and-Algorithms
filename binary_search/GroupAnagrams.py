# Problem: Group Anagrams
# Date: 16/3/2026

# Approach: Tuple of character counts as HashMap key
# Time: O(n * k) - n words, k is average word length
# Space: O(n) - hashmap stores all words

# Mental analogy: 26 empty boxes representing each character.
# Each word places balls in boxes according to letter frequency.
# Words with same number of balls in same boxes get grouped together.
# That pattern of balls becomes the key, the group is the value.

class Solution:
    def groupAnagrams(self, strs):
        hashmap = {}
        for word in strs:
            alpha_count = [0] * 26
            for letter in word:
                alpha_count[ord(letter) - ord("a")] += 1
            key = tuple(alpha_count)
            if key not in hashmap:
                hashmap[key] = [word]
            else:
                hashmap[key].append(word)
        return list(hashmap.values())