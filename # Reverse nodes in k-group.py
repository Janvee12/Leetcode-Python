# ============================
# PLATFORM:
# LeetCode (Problem 25 - Reverse Nodes in k-Group)
# ============================

# ============================
# PROBLEM:
# Given the head of a linked list,
# reverse nodes of the list
# k at a time.
#
# If the number of nodes left
# is less than k,
# leave them as it is.
#
# Example:
#
# Input:
# head = [1,2,3,4,5]
# k = 2
#
# Output:
# [2,1,4,3,5]
#
# Example:
#
# Input:
# head = [1,2,3,4,5]
# k = 3
#
# Output:
# [3,2,1,4,5]
# ============================

# ============================
# APPROACH:
#
# Use POINTER MANIPULATION
#
# Steps:
#
# 1. Create dummy node.
#
# 2. For every group:
#
#    - Find kth node.
#
#    - Reverse nodes in that group.
#
#    - Connect reversed group
#      with previous and next parts.
#
# 3. Continue until
#    fewer than k nodes remain.
#
# ============================

# ============================
# KEY IDEA:
#
# Reverse linked list section:
#
# prev <- curr <- next
#
# using iterative reversal.
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

    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        # Dummy node
        dummy = ListNode(0, head)

        # Previous group pointer
        groupPrev = dummy

        while True:

            # Find kth node
            Kth = self.getKth(groupPrev, k)

            # Not enough nodes
            if not Kth:

                break

            # Next group start
            groupNext = Kth.next

            # Reverse current group
            prev = Kth.next

            curr = groupPrev.next

            while curr != groupNext:

                tmp = curr.next

                curr.next = prev

                prev = curr

                curr = tmp

            # Connect reversed group
            tmp = groupPrev.next

            groupPrev.next = Kth

            groupPrev = tmp

        return dummy.next

    # Find kth node from current
    def getKth(self, curr, k):

        while curr and k > 0:

            curr = curr.next

            k -= 1

        return curr