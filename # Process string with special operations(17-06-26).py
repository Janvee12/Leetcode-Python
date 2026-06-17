# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# Process String with Operations
# (Optimized Query Version)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Operations:
#
# lowercase letter
#   -> append character
#
# '*'
#   -> remove last character
#
# '#'
#   -> duplicate current string
#
# '%'
#   -> reverse current string
#
# Return the character at index k
# after all operations.
#
# If k is out of bounds:
#
#     return '.'
#
# ============================
# APPROACH:
# ============================
#
# Building the final string can be huge.
#
# Instead:
#
# 1. First calculate final length.
#
# 2. Traverse operations backwards.
#
# 3. Map index k back to the character
#    that originally produced it.
#
# This avoids constructing the string.
#
# ============================

class Solution:

    def processStr(self, s: str, k: int) -> str:

        # ============================
        # STEP 1:
        # Calculate final length
        # ============================
        length = 0

        for c in s:

            if c.islower():
                length += 1

            elif c == '*' and length:
                length -= 1

            elif c == '#':
                length *= 2

            elif c == '%':
                pass

        # ============================
        # k outside final string
        # ============================
        if k >= length:
            return '.'

        # ============================
        # STEP 2:
        # Reverse simulation
        # ============================
        for c in reversed(s):

            # ------------------------
            # Character insertion
            # ------------------------
            if c.islower():

                if k == length - 1:
                    return c

                length -= 1

            # ------------------------
            # Undo delete
            # ------------------------
            elif c == '*':
                length += 1

            # ------------------------
            # Undo duplication
            # ------------------------
            elif c == '#':

                length //= 2

                if k >= length:
                    k -= length

            # ------------------------
            # Undo reverse
            # ------------------------
            elif c == '%':

                k = length - 1 - k