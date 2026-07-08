# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# Sum and Multiply
# ============================

from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Prefix arrays
        prefix_sum = [0] * n          # Sum of digits
        prefix_count = [0] * n        # Count of non-zero digits
        prefix_number = [0] * n       # Number formed by non-zero digits

        # Initialize first digit
        d = int(s[0])
        prefix_sum[0] = d
        prefix_count[0] = 1 if d != 0 else 0
        prefix_number[0] = d if d != 0 else 0

        # Build prefix arrays
        for i in range(1, n):
            d = int(s[i])

            prefix_sum[i] = (prefix_sum[i - 1] + d) % MOD
            prefix_count[i] = prefix_count[i - 1] + (1 if d != 0 else 0)

            if d != 0:
                prefix_number[i] = (prefix_number[i - 1] * 10 + d) % MOD
            else:
                prefix_number[i] = prefix_number[i - 1]

        answer = []

        for left, right in queries:

            # Sum of digits in the range
            digit_sum = (
                prefix_sum[right]
                - (prefix_sum[left - 1] if left > 0 else 0)
            ) % MOD

            # Number of non-zero digits
            non_zero = (
                prefix_count[right]
                - (prefix_count[left - 1] if left > 0 else 0)
            )

            # Number formed after removing zeros
            number = (
                prefix_number[right]
                - (
                    prefix_number[left - 1]
                    * pow(10, non_zero, MOD)
                    if left > 0
                    else 0
                )
            ) % MOD

            answer.append((number * digit_sum) % MOD)

        return answer