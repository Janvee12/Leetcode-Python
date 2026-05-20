# ============================
# PLATFORM:
# LeetCode (Problem 24 - Swap Nodes in Pairs)
# ============================

# ============================
# PROBLEM:
# Given a linked list,
# swap every two adjacent nodes
# and return its head.
#
# You must swap nodes themselves,
# not just their values.
#
# Example:
#
# Input:
# head = [1,2,3,4]
#
# Output:
# [2,1,4,3]
# ============================

# ============================
# APPROACH:
#
# Use POINTER MANIPULATION
#
# Steps:
#
# 1. Create a dummy node
#    before head.
#
# 2. Use:
#
#       prev -> node before pair
#       curr -> first node of pair
#
# 3. Identify:
#
#       second = curr.next
#       nxtPair = curr.next.next
#
# 4. Perform swapping:
#
#       second.next = curr
#       curr.next = nxtPair
#       prev.next = second
#
# 5. Move pointers forward.
#
# ============================

# ============================
# VISUAL:
#
# Before:
# prev -> 1 -> 2 -> 3 -> 4
#
# After:
# prev -> 2 -> 1 -> 3 -> 4
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def swapPairs(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node before head
        dummy = ListNode(0, head)

        prev = dummy
        curr = head

        # Process pairs
        while curr and curr.next:

            # Nodes needed for swapping
            nxtPair = curr.next.next

            second = curr.next

            # Swap nodes
            second.next = curr

            curr.next = nxtPair

            prev.next = second

            # Move pointers
            prev = curr

            curr = nxtPair

        return dummy.next