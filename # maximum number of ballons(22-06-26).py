# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 1189. Maximum Number of Balloons
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given a string text,
# return the maximum number
# of times we can form the
# word:
#
# "balloon"
#
# Each character can be used
# only once.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Count the frequency of:
#
# b, a, l, o, n
#
# The word "balloon" needs:
#
# b -> 1
# a -> 1
# l -> 2
# o -> 2
# n -> 1
#
# Therefore:
#
# answer =
# min(
#     count(b),
#     count(a),
#     count(l) // 2,
#     count(o) // 2,
#     count(n)
# )
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        freq = defaultdict(int)

        # Count useful characters
        for ch in text:
            if ch in "balloon":
                freq[ch] += 1

        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n']
        )