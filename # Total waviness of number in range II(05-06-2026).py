# ============================
# PLATFORM:
# Custom / LeetCode Hard (Digit DP attempt)
# Problem: Total Waviness
# ============================

# ============================
# PROBLEM STATEMENT:
# ============================
# Given two integers num1 and num2,
# count total "waviness points" in
# all numbers in range [num1, num2].
#
# A waviness point exists at index i:
#
#   s[i-1] < s[i] > s[i+1]   (peak)
#   OR
#   s[i-1] > s[i] < s[i+1]   (valley)
#
# ============================
# YOUR IDEA:
# ============================
#
# You tried to solve it using:
#
# ✔ Digit DP
# ✔ Range DP (sum_up_to)
# ✔ Trend tracking
#
# ============================
# WHAT YOUR CODE IS DOING:
# ============================

# ----------------------------
# 1. sum_same_len(limit)
# ----------------------------
# tries to compute:
#   contribution for numbers
#   of same digit length
#
# using digit DP:
#
# dp(i, prev, tight, curr, trend)

# ----------------------------
# 2. dp state meaning:
# ----------------------------
# i      -> digit position
# prev   -> previous digit
# tight  -> limit constraint
# curr   -> waviness count so far
# trend  -> direction (up/down)
#
# ----------------------------

# ============================
# CRITICAL MISTAKES:
# ============================

# ❌ MISTAKE 1: WRONG STATE MODEL
#
# Waviness depends on:
#   (prev2, prev1, curr)
#
# BUT your DP uses:
#   only prev + trend
#
# trend is NOT enough information.

# Example:
#   2 5 3 → peak at 5
#   5 1 4 → valley at 1
#
# Trend cannot distinguish these reliably.

# ============================

# ❌ MISTAKE 2: DOUBLE COUNTING STRUCTURE
#
# You do:
#
# sum_up_to(num2) - sum_up_to(num1)
#
# then again:
#
# manual check on num1
#
# → indicates inconsistent DP logic

# ============================

# ❌ MISTAKE 3: DP OVERCOMPRESSION
#
# You compressed 3-digit problem into:
#   1-digit memory (prev)
#
# But waviness is a LOCAL 3-window pattern:
#
#   s[i-1], s[i], s[i+1]
#
# DP cannot "predict" future i+1 digit
# without storing 2 previous digits.

# ============================

# ❌ MISTAKE 4: trend logic is incorrect
#
# This part:
#
# if trend == 1 and d < prev: ncurr += 1
# elif trend == 2 and d > prev: ncurr += 1
#
# is NOT valid waviness detection.
#
# It assumes:
#   trend change → waviness
#
# But waviness is:
#   strict peak/valley structure

# ============================
# CORRECT INSIGHT:
# ============================
#
# Waviness is a 3-digit condition:
#
#   prev2, prev1, curr
#
# So correct DP state MUST be:
#
#   dp(i, prev2, prev1, tight)
#
# and transition checks:
#
#   if prev2 < prev1 > curr → +1
#   if prev2 > prev1 < curr → +1

# ============================
# CORRECT APPROACH (BRUTE FORCE):
# ============================

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        res = 0

        for n in range(num1, num2 + 1):
            s = str(n)

            for i in range(1, len(s) - 1):

                if (
                    s[i - 1] < s[i] > s[i + 1]
                    or
                    s[i - 1] > s[i] < s[i + 1]
                ):
                    res += 1

        return res


# ============================
# WHY BRUTE FORCE IS BEST HERE:
# ============================
#
# ✔ Directly matches definition
# ✔ No hidden state tracking needed
# ✔ No DP complexity errors
# ✔ Guaranteed correct

# ============================
# TIME COMPLEXITY:
# ============================
# O(N * D)
# N = range size
# D = number of digits
#
# ============================
# SPACE COMPLEXITY:
# ============================
# O(1)
#
# ============================

# ============================
# FINAL VERDICT:
# ============================
#
# ❌ Your DP approach = incorrect modeling
# ✔ Brute force = correct solution
#
# If constraints were huge,
# we would redesign DP using:
#
#   prev2 + prev1 state machine
#
# ============================