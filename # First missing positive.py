# ============================
# PLATFORM:
# LeetCode
# (41. First Missing Positive)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an unsorted array A,
# find the smallest missing positive integer.
#
# Constraints idea:
# - Must be O(n) time
# - Must use O(1) extra space
#
# ============================
# APPROACH USED HERE:
# ============================
#
# We use the array itself as a hash map.
#
# Idea:
# If number x exists,
# mark index (x-1) in array.
#
# ============================
# STEP 1: CLEAN NEGATIVES
# ============================
#
# Replace all negative numbers with 0
# because they are useless for answer.
#

for i in range(len(A)):
    if A[i] < 0:
        A[i] = 0


# ============================
# STEP 2: MARK VISITED NUMBERS
# ============================
#
# For each value val:
# if 1 <= val <= n:
#   mark A[val-1]
#
# Marking rule:
#
# - if positive → make negative
# - if zero → set special marker (-n-1)
#
# This preserves information safely.
#

for i in range(len(A)):

    val = abs(A[i])

    if 1 <= val <= len(A):

        # mark index val-1 as visited
        if A[val - 1] > 0:
            A[val - 1] *= -1

        elif A[val - 1] == 0:
            A[val - 1] = -(len(A) + 1)


# ============================
# STEP 3: FIND FIRST MISSING
# ============================
#
# First index that is NOT negative
# means that number is missing.
#

for i in range(1, len(A) + 1):
    if A[i - 1] >= 0:
        return i


# ============================
# STEP 4: EDGE CASE
# ============================
#
# If all numbers 1..n exist,
# answer is n+1
#

return len(A) + 1