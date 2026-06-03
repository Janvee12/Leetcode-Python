# ============================
# PLATFORM:
# LeetCode
# (Problem 38 - Count and Say)
# ============================

# ============================
# PROBLEM
# ============================
#
# The Count-and-Say sequence:
#
# n = 1 -> "1"
#
# n = 2 -> "11"
#        (one 1)
#
# n = 3 -> "21"
#        (two 1s)
#
# n = 4 -> "1211"
#        (one 2, one 1)
#
# n = 5 -> "111221"
#        (one 1, one 2,
#         two 1s)
#
# Return the nth term.
#
# ============================

# ============================
# APPROACH
# ============================
#
# Recursively generate
# the previous term.
#
# Then "read" it:
#
# Count consecutive
# identical digits.
#
# Append:
#
# count + digit
#
# to form the next term.
#
# ============================

class Solution:

    def countAndSay(self, n: int) -> str:

        # Base case
        if n == 1:
            return "1"

        # Generate previous term
        prev = self.countAndSay(n - 1)

        result = ""
        count = 1

        # Read previous term
        for i in range(len(prev)):

            if (
                i + 1 < len(prev)
                and prev[i] == prev[i + 1]
            ):
                count += 1

            else:
                result += (
                    str(count)
                    + prev[i]
                )

                count = 1

        return result