# Problem: Valid Parentheses
# Date: 15 Sep 2026

# Approach: Use a stack and a hashmap - LIFO
# Time: O(n) - single pass through the string
# Space: O(n) - stack can grow up to n/2 in the worst case

# Mental model: If there is a shoe rack and if you find a left-leg shoe, you put it on the rack.
# Every left-leg shoe goes on top of each other. The moment you find a right-leg shoe, you check
# the top of the rack. If it matches, great pair, remove it. If it doesn't, bad pair, invalid.


class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #Create a stack (A Python list works well as a stack)
        hashmap={"]":"[", "}":"{" , ")":"("} #Mapping the closing brackets to opening brackets
        if len(s)%2 != 0: #A string with odd number of brackets will never be valid parentheses
            return False
        for str in s: #Main loop
            if str not in hashmap: #if str is not in hashmap(keys), then it is an opening bracket
                stack.append(str) #add the opening bracket to the top of the stack.
            else: #the str is a closing bracket
                if stack and hashmap[str] == stack[-1]: #if stack is non empty and the matching opening bracket of the current closing bracket
                    stack.pop()                         #is the last one to be added to stack, then we get a pair and we pop from stack
                else:
                    return False

        if len(stack)!=0: #If any openign bracket is left in the stack, then it is not a valid parentheses
            return False
        return True        

# We follow the LIFO principle : the last opening bracket added to the stack should be the matching pair for the current closing bracket.

# Is the chosen closing bracket's matching opening bracket on the top of my stack - CHECK

# A given stirng may start with a closing bracket and a check for opening bracket at that point will go through an empty stack
#so we have to prevent the crash by introducing an empty stack check.