# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 49. Group Anagrams
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an array of strings,
# group all anagrams together.
#
# Two strings are anagrams if
# they contain the same letters
# with the same frequency.
#
# Example:
#
# Input:
# ["eat","tea","tan","ate","nat","bat"]
#
# Output:
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Anagrams have identical
# character frequencies.
#
# Create a frequency array
# of size 26 for each word.
#
# Example:
#
# "eat"
#
# a -> 1
# e -> 1
# t -> 1
#
# Convert the frequency array
# into a tuple and use it as
# a dictionary key.
#
# Words with the same frequency
# array belong to the same group.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n × k)
#
# n = number of strings
# k = average string length
#
# SPACE COMPLEXITY:
# O(n)
# ============================

from typing import List
from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:

            # Frequency array
            count = [0] * 26

            # Count characters
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            # Use tuple as dictionary key
            groups[tuple(count)].append(word)

        return list(groups.values())