# ============================
# PLATFORM:
# LeetCode (Problem 23 - Merge k Sorted Lists)
# ============================

# ============================
# PROBLEM:
# You are given an array of k
# sorted linked lists.
#
# Merge all linked lists into
# one sorted linked list
# and return its head.
#
# Example:
#
# Input:
# lists = [
#   [1,4,5],
#   [1,3,4],
#   [2,6]
# ]
#
# Output:
# [1,1,2,3,4,4,5,6]
# ============================

# ============================
# APPROACH:
#
# Use MIN HEAP (Priority Queue)
#
# Steps:
#
# 1. Insert first node of every list
#    into min heap.
#
# 2. Heap stores:
#
#       (node value, index, node)
#
#    index avoids comparison error
#    between ListNode objects.
#
# 3. Pop smallest node from heap.
#
# 4. Attach it to merged list.
#
# 5. If popped node has next node:
#       push next node into heap.
#
# 6. Continue until heap becomes empty.
#
# ============================

# ============================
# WHY HEAP?
#
# Heap always gives the smallest node
# in O(log k) time.
#
# Efficient for merging multiple lists.
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(N log k)
#
# N = total nodes
# k = number of linked lists
#
# SPACE COMPLEXITY:
# O(k)
# → heap storage
# ============================

import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        # Min heap
        heap = []

        # Add first node of each list
        for i, l in enumerate(lists):

            if l:

                heapq.heappush(
                    heap,
                    (l.val, i, l)
                )

        # Dummy node
        dummy = ListNode(0)

        tail = dummy

        # Process heap
        while heap:

            # Smallest node
            val, i, node = heapq.heappop(heap)

            # Attach node
            tail.next = node

            tail = tail.next

            # Push next node if exists
            if node.next:

                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next