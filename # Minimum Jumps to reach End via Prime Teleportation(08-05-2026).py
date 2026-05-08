# ============================
# PLATFORM:
# LeetCode (Graph / BFS / Number Theory)
# ============================

# ============================
# PROBLEM:
# Given an array nums,
# you start from index 0 and want to reach index n-1
# using minimum jumps.
#
# Allowed moves:
# 1. Move to i + 1
# 2. Move to i - 1
# 3. Jump to another index sharing a common prime factor
#
# Return minimum jumps needed to reach last index.
#
# This solution uses:
# - Sieve of Eratosthenes
# - Smallest Prime Factor (SPF)
# - BFS (Breadth First Search)
# ============================

# ============================
# APPROACH:
#
# PART 1: PRECOMPUTE PRIME FACTORS
#
# We build:
# - sieve[] → prime checking
# - spf[]   → smallest prime factor
#
# Using SPF:
# - Prime factorization becomes very fast.
#
# Example:
# x = 12
# SPF path:
# 12 → 2
# 6  → 2
# 3  → 3
#
# Prime factors = {2, 3}
#
# ------------------------------------------------
# PART 2: GROUP INDICES BY PRIME FACTORS
#
# Example:
# nums = [6,10,15]
#
# Prime groups:
# 2 → [0,1]
# 3 → [0,2]
# 5 → [1,2]
#
# ------------------------------------------------
# PART 3: BFS
#
# From each index:
# - move left
# - move right
# - jump to all indices sharing prime factors
#
# BFS guarantees minimum jumps.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# Sieve:
# O(M log log M)
#
# BFS + factorization:
# Approximately O(n log M)
#
# SPACE COMPLEXITY:
# O(M + n)
#
# M = maximum number value
# ============================

from typing import List
from collections import defaultdict, deque

# ============================
# SIEVE + SPF PRECOMPUTATION
# ============================

MX = 10**6 + 10

sieve = [True] * MX
sieve[0], sieve[1] = False, False

# Smallest Prime Factor
spf = [0] * MX

for i in range(2, MX):

    if sieve[i]:

        spf[i] = i

        for j in range(i + i, MX, i):

            sieve[j] = False

            # store smallest prime factor
            if spf[j] == 0:
                spf[j] = i


# ============================
# GET PRIME FACTORS
# ============================

def get_factors(x):

    res = set()

    while x > 1:

        p = spf[x]

        res.add(p)

        x //= p

    return res


# ============================
# SOLUTION
# ============================

class Solution:

    def minJumps(self, nums: List[int]) -> int:

        n = len(nums)

        # prime_factor -> indices
        groups = defaultdict(list)

        # Build groups
        for i, x in enumerate(nums):

            for p in get_factors(x):
                groups[p].append(i)

        # BFS queue: (index, jumps)
        q = deque()
        q.append((0, 0))

        # Visited indices
        seen_i = set()
        seen_i.add(0)

        # Visited prime groups
        seen_p = set()

        while q:

            i, jumps = q.popleft()

            # Reached destination
            if i == n - 1:
                return jumps

            # ============================
            # Move Right
            # ============================
            if i + 1 < n and (i + 1) not in seen_i:

                q.append((i + 1, jumps + 1))
                seen_i.add(i + 1)

            # ============================
            # Move Left
            # ============================
            if i - 1 >= 0 and (i - 1) not in seen_i:

                q.append((i - 1, jumps + 1))
                seen_i.add(i - 1)

            # ============================
            # Prime Factor Jumps
            # ============================
            for p in get_factors(nums[i]):

                if p not in seen_p:

                    seen_p.add(p)

                    for j in groups[p]:

                        if j not in seen_i:

                            q.append((j, jumps + 1))
                            seen_i.add(j)

        return -1