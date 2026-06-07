# ============================
# PLATFORM:
# LeetCode
# (Create Binary Tree from Descriptions)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given a list of descriptions:
#
#   [parent, child, isLeft]
#
# meaning:
# - parent has a child
# - if isLeft == 1 → left child
# - else → right child
#
# You must construct the binary tree
# and return the ROOT node.
#
# ============================
# APPROACH:
# ============================
#
# 1. Use a hashmap to store nodes
# 2. Track all children nodes
# 3. Root is the node that is NEVER a child
#
# ============================


# Tree node definition
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def createBinaryTree(self, descriptions):

        # ============================
        # STEP 1: Storage
        # ============================
        nodes = {}       # value -> TreeNode
        children = set() # all child nodes

        # helper to create/reuse node
        def get_node(val):
            if val not in nodes:
                nodes[val] = TreeNode(val)
            return nodes[val]

        # ============================
        # STEP 2: Build tree
        # ============================
        for parent, child, isLeft in descriptions:

            parent_node = get_node(parent)
            child_node = get_node(child)

            if isLeft == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

            # mark as child
            children.add(child)

        # ============================
        # STEP 3: Find root
        # ============================
        # root = node that never appears as child
        root_val = (set(nodes.keys()) - children).pop()

        return nodes[root_val]