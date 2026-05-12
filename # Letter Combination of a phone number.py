# ============================
# PLATFORM:
# LeetCode (Problem 17 - Letter Combinations of a Phone Number)
# ============================

# ============================
# PROBLEM:
# Given a string containing digits from 2-9,
# return all possible letter combinations
# that the number could represent.
#
# Phone keypad mapping:
#
# 2 -> abc
# 3 -> def
# 4 -> ghi
# 5 -> jkl
# 6 -> mno
# 7 -> pqrs
# 8 -> tuv
# 9 -> wxyz
#
# Example:
# Input:
# digits = "23"
#
# Output:
# [
#   "ad","ae","af",
#   "bd","be","bf",
#   "cd","ce","cf"
# ]
# ============================

# ============================
# APPROACH:
#
# Use BACKTRACKING
#
# Steps:
#
# 1. Create digit-to-letter mapping.
#
# 2. Start from first digit.
#
# 3. For every letter of current digit:
#    - add letter to current combination
#    - recursively process next digit
#
# 4. Base Case:
#    When combination length equals
#    digits length:
#       store result
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(4^n)
#
# Each digit can generate:
# - 3 letters
# - or 4 letters
#
# SPACE COMPLEXITY:
#
# O(n)
# → recursion stack
# ============================

from typing import List

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        # Edge case
        if not digits:
            return []

        # Phone keypad mapping
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        # Store final combinations
        res = []

        # ============================
        # Backtracking Function
        # ============================
        def backtrack(idx, comb):

            # Base case
            if len(comb) == len(digits):

                res.append(comb)

                return

            # Explore letters of current digit
            for letter in digit_to_letters[digits[idx]]:

                backtrack(idx + 1, comb + letter)

        # Start recursion
        backtrack(0, "")

        return res