# ============================
# PLATFORM:
# LeetCode
# ============================
# PROBLEM:
# Rotate List
# ============================

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        # Handle empty list
        if not head:
            return head

        # Find the length of the list and the last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Reduce unnecessary rotations
        k %= length

        if k == 0:
            return head

        # Find the new tail
        current = head
        for _ in range(length - k - 1):
            current = current.next

        # Update pointers to rotate the list
        new_head = current.next
        current.next = None
        tail.next = head

        return new_head