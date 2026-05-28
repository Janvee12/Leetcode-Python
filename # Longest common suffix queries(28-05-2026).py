# ============================
# PLATFORM:
# LeetCode
# (Problem 3093 - Longest Common Suffix Queries)
# ============================

# ============================
# PROBLEM:
# You are given:
#
#     wordsContainer
#     wordsQuery
#
# For every query word:
#
# Find the index of the string
# in wordsContainer that:
#
# 1. Shares the LONGEST suffix
#    with the query word.
#
# 2. If multiple exist:
#       choose shortest string.
#
# 3. If still tied:
#       choose smallest index.
#
# Return answer for all queries.
# ============================

# ============================
# APPROACH:
#
# Use a TRIE on REVERSED strings.
#
# Why reverse?
#
# Because:
#
# suffix matching
# becomes
# prefix matching.
#
# Example:
#
# "coding" -> "gnidoc"
# "ding"   -> "gnid"
#
# Common suffix:
# "ding"
#
# becomes common prefix:
# "gnid"
#
# ============================

# ============================
# TRIE NODE STORES:
#
# children -> next characters
#
# smallest -> shortest word length
#             passing through node
#
# idx -> index of that word
#
# This helps quickly return
# correct answer during query.
# ============================

# ============================
# INSERT:
#
# Insert reversed word
# character by character.
#
# Update:
#
# - smallest length
# - corresponding index
#
# ============================

# ============================
# QUERY:
#
# Traverse trie using
# reversed query string.
#
# Stop when character missing.
#
# Return stored best index.
# ============================

# ============================
# TIME COMPLEXITY:
#
# Insert:
# O(total characters)
#
# Query:
# O(total query characters)
#
# SPACE COMPLEXITY:
# O(total characters)
# ============================

from math import inf
from typing import List

# ============================
# Trie Node
# ============================

class TrieNode:

    def __init__(self):

        # Child nodes
        self.children = {}

        # Shortest word length
        self.smallest = inf

        # Corresponding index
        self.idx = inf


# ============================
# Trie Class
# ============================

class Trie:

    def __init__(self):

        self.root = TrieNode()

    # Insert reversed string
    def insert(self, s, idx):

        curr = self.root

        # Update root info
        if len(s) < curr.smallest:

            curr.smallest = len(s)

            curr.idx = idx

        # Insert characters
        for c in s:

            if c not in curr.children:

                curr.children[c] = TrieNode()

            curr = curr.children[c]

            # Update shortest string info
            if len(s) < curr.smallest:

                curr.smallest = len(s)

                curr.idx = idx

    # Query reversed string
    def query(self, s):

        curr = self.root

        for c in s:

            # Stop if path breaks
            if c not in curr.children:

                break

            curr = curr.children[c]

        return curr.idx


# ============================
# Solution
# ============================

class Solution:

    def stringIndices(
        self,
        wordsContainer: List[str],
        wordsQuery: List[str]
    ) -> List[int]:

        trie = Trie()

        res = []

        # Insert reversed container words
        for i, w in enumerate(wordsContainer):

            trie.insert(w[::-1], i)

        # Process queries
        for w in wordsQuery:

            res.append(
                trie.query(w[::-1])
            )

        return res