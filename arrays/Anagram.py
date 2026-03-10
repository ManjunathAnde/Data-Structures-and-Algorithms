# Problem: Valid Anagram
# Date: 10/3/2026

# Approach: HashMap character counting
# Time: O(n) - one pass through each string
# Space: O(1) - hashmap stores at most 26 characters.
#As we are storing no of occurences of each alphabet(26)

# Mental analogy: Put one ball beside each alphabet as we
#encounter them in first word. Then kick the ball(s) away
#as we get encounter those alphabets each time in second word.
#If no balls are left at the end, the words are anagrams. 

class Solution:
    def isAnagram(self, s: str, t: str):
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        for letter in t:
            if letter not in hashmap:
                return False
            else:
                hashmap[letter] -= 1
        for val in hashmap.values():
            if val != 0:
                return False
        return True