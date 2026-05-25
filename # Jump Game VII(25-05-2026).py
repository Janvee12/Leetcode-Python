# ============================
# PLATFORM:
# LeetCode
# (Problem 1871 - Jump Game VII)
# ============================

# ============================
# PROBLEM:
# You are given:
#
#     s        -> binary string
#     minJump
#     maxJump
#
# Start at index 0.
#
# You can jump from index i
# to index j if:
#
# 1. i + minJump <= j <= i + maxJump
#
# 2. s[j] == '0'
#
# Task:
# Return True if you can reach
# the last index.
#
# Example:
#
# Input:
# s = "011010"
# minJump = 2
# maxJump = 3
#
# Output:
# True
# ============================

# ============================
# APPROACH:
#
# Use BFS
#
# Key Optimization:
#
# Avoid rechecking ranges
# using "farthest".
#
# Steps:
#
# 1. Start BFS from index 0.
#
# 2. For each index i:
#
#    explore:
#
#       [i + minJump,
#        i + maxJump]
#
# 3. Only visit:
#
#       s[j] == '0'
#
# 4. Use farthest
#    to avoid repeated scanning.
#
# ============================

# ============================
# WHY farthest?
#
# Without it:
# many ranges overlap,
# causing TLE.
#
# farthest stores
# the maximum already explored index.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

from collections import deque

class Solution:

    def canReach(
        self,
        s: str,
        minJump: int,
        maxJump: int
    ) -> bool:

        # BFS queue
        q = deque([0])

        # Farthest explored index
        farthest = 0

        # BFS traversal
        while q:

            i = q.popleft()

            # Start of new range
            start = max(
                i + minJump,
                farthest + 1
            )

            # Explore reachable positions
            for j in range(
                start,
                min(i + maxJump + 1, len(s))
            ):

                # Valid jump
                if s[j] == "0":

                    q.append(j)

                    # Reached destination
                    if j == len(s) - 1:

                        return True

            # Update explored boundary
            farthest = i + maxJump

        return False