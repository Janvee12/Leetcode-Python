# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# Process String with Special Operations
# ============================

# ============================
# APPROACH:
#
# Traverse the string character by character.
#
# Rules:
#
# 1. Lowercase letter:
#    Add it to the result.
#
# 2. '*':
#    Remove the last character
#    if result is not empty.
#
# 3. '#':
#    Duplicate the current result.
#
# 4. '%':
#    Reverse the current result.
#
# Use a list because:
# - append() is O(1)
# - pop() is O(1)
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + operations)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

class Solution:
    def processStr(self, s: str) -> str:

        arr = []

        for c in s:

            # Add lowercase character
            if c.islower():
                arr.append(c)

            # Remove last character
            elif c == '*' and arr:
                arr.pop()

            # Duplicate current string
            elif c == '#':
                arr += arr

            # Reverse current string
            elif c == '%':
                arr = arr[::-1]

        return "".join(arr)