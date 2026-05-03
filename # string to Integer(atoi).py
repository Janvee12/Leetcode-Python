# ============================
# PLATFORM:
# LeetCode (Problem 8 - String to Integer (atoi))
# ============================

# ============================
# PROBLEM:
# Implement the function myAtoi(string s),
# which converts a string to a 32-bit signed integer.
#
# Rules:
# 1. Ignore leading whitespace.
# 2. Check optional sign (+ or -).
# 3. Read digits until a non-digit character appears.
# 4. Ignore remaining characters.
# 5. Clamp result within 32-bit signed integer range:
#       [-2^31, 2^31 - 1]
#
# Example:
# Input: "   -42"
# Output: -42
#
# Input: "4193 with words"
# Output: 4193
#
# Input: "words and 987"
# Output: 0
# ============================

# ============================
# APPROACH:
# 1. Remove leading spaces using lstrip().
# 2. Check sign (+ or -).
# 3. Iterate through characters:
#    - If digit → build number
#    - Else → stop parsing
# 4. Apply sign to result.
# 5. Handle overflow by clamping value.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Traverse string once
#
# SPACE COMPLEXITY:
# O(1)
# → No extra space used
# ============================

class Solution:
    def myAtoi(self, s: str) -> int:

        # Step 1: Remove leading spaces
        s = s.lstrip()

        if not s:
            return 0

        i = 0
        sign = 1

        # Step 2: Handle sign
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        parsed = 0

        # Step 3: Parse digits
        while i < len(s):
            cur = s[i]

            if not cur.isdigit():
                break

            parsed = parsed * 10 + int(cur)
            i += 1

        # Step 4: Apply sign
        parsed *= sign

        # Step 5: Clamp within 32-bit integer range
        if parsed > 2**31 - 1:
            return 2**31 - 1
        elif parsed < -2**31:
            return -2**31
        else:
            return parsed