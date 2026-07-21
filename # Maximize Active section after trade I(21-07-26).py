# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Maximum Active Sections After Trade
# ============================

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        n = len(s)

        # Count active sections ('1') and store lengths of zero blocks
        active_count = 0
        zero_blocks = []

        index = 0
        while index < n:

            if s[index] == "0":
                start = index

                while index < n and s[index] == "0":
                    index += 1

                zero_blocks.append(index - start)

            else:
                active_count += 1
                index += 1

        # If fewer than two zero blocks exist, no beneficial trade is possible
        if len(zero_blocks) < 2:
            return active_count

        # Find the maximum sum of two consecutive zero blocks
        max_gain = 0

        for i in range(1, len(zero_blocks)):
            max_gain = max(max_gain, zero_blocks[i - 1] + zero_blocks[i])

        return active_count + max_gain