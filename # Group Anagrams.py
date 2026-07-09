# ============================
# PLATFORM:
# LeetCode 49
# PROBLEM:
# Group Anagrams
# ============================

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:

            # Frequency of each letter
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            # Use frequency tuple as the key
            groups[tuple(count)].append(word)

        return list(groups.values())