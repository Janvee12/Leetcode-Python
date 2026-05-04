# ============================
# PLATFORM:
# LeetCode (Problem 9 - Palindrome Number)
# ============================

# ============================
# PROBLEM:
# Given an integer x, return True if x is a palindrome,
# and False otherwise.
#
# A palindrome number reads the same forward and backward.
#
# Example:
# Input: x = 121
# Output: True
#
# Input: x = -121
# Output: False
#
# Input: x = 10
# Output: False
# ============================

# ============================
# APPROACH:
#
# 1. Negative numbers are not palindrome → return False.
#
# 2. Find divisor to extract leftmost digit:
#    - Example: 12321 → div = 10000
#
# 3. Compare:
#    - left digit (x // div)
#    - right digit (x % 10)
#
# 4. If not equal → return False
#
# 5. Remove both digits:
#    - x = (x % div) // 10
#    - div = div // 100
#
# 6. Repeat until number becomes 0
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(log10(n))
# → Number of digits
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are not palindrome
        if x < 0:
            return False

        # Find divisor
        div = 1
        while x >= 10 * div:
            div *= 10

        while x:

            # Extract digits
            left = x // div
            right = x % 10

            # Compare
            if left != right:
                return False

            # Remove left and right digits
            x = (x % div) // 10

            # Reduce divisor
            div //= 100   # IMPORTANT: integer division

        return True