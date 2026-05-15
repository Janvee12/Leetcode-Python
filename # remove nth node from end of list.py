# ============================
# PLATFORM:
# LeetCode (Problem 19 - Remove Nth Node From End of List)
# ============================

# ============================
# PROBLEM:
# Given the head of a linked list,
# remove the nth node from the end
# of the list and return its head.
#
# Example:
# Input:
# head = [1,2,3,4,5]
# n = 2
#
# Output:
# [1,2,3,5]
#
# Explanation:
# The 2nd node from the end is 4,
# so remove it.
# ============================

# ============================
# APPROACH:
#
# Use TWO POINTERS
#
# Steps:
#
# 1. Create a dummy node before head.
#
# 2. Use two pointers:
#       left
#       right
#
# 3. Move right pointer n steps ahead.
#
# 4. Move both pointers together
#    until right reaches end.
#
# 5. Now:
#       left.next
#    is the node to remove.
#
# 6. Skip the node:
#
#       left.next = left.next.next
#
# ============================

# ============================
# WHY DUMMY NODE?
#
# Helps handle edge cases easily,
# especially when deleting the head node.
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

    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        # Dummy node before head
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0 and right:

            right = right.next
            n -= 1

        # Move both pointers together
        while right:

            left = left.next
            right = right.next

        # Remove target node
        left.next = left.next.next

        return dummy.next