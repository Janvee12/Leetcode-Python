# ============================
# PLATFORM:
# LeetCode (Problem 61 - Rotate List)
# ============================

# ============================
# PROBLEM:
# Given the head of a linked list, rotate the list to the right by k places.
#
# Example:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
# Explanation:
# Rotate right by 2 → last 2 nodes move to front.
# ============================

# ============================
# APPROACH:
#
# 1. Handle edge case:
#    - If head is None → return head
#
# 2. Find length of list and last node (tail).
#
# 3. Optimize k:
#    - k = k % length (avoid unnecessary rotations)
#
# 4. If k == 0 → no rotation needed.
#
# 5. Find new tail:
#    - It will be at position (length - k - 1)
#
# 6. New head = next of new tail
#
# 7. Break link:
#    - newTail.next = None
#
# 8. Connect old tail to old head:
#    - tail.next = head
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Traverse list to find length and split point
#
# SPACE COMPLEXITY:
# O(1)
# → No extra space used
# ============================

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge case
        if not head:
            return head

        # Step 1: Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize k
        k = k % length

        if k == 0:
            return head

        # Step 3: Find new tail (length - k - 1)
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next

        # Step 4: New head
        newHead = cur.next

        # Step 5: Break the list
        cur.next = None

        # Step 6: Connect tail to old head
        tail.next = head

        return newHead