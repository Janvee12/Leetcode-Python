# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 1344. Angle Between Hands of a Clock
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given:
#   hour    -> hour hand position
#   minutes -> minute hand position
#
# Return the smaller angle
# between the hour hand and
# minute hand.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Minute Hand:
#
# Every minute = 6 degrees
#
# Therefore:
#
# minute_angle = minutes * 6
#
#
# Hour Hand:
#
# Every hour = 30 degrees
#
# But the hour hand also moves
# continuously as minutes pass.
#
# Therefore:
#
# hour_angle =
#     (hour * 30)
#     + (minutes * 0.5)
#
#
# Compute:
#
# difference =
#     |hour_angle - minute_angle|
#
# Since a circle has 360°:
#
# answer =
#     min(
#         difference,
#         360 - difference
#     )
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # Hour hand angle
        hour_angle = (hour * 30) + (0.5 * minutes)

        # Minute hand angle
        minute_angle = minutes * 6

        # Absolute difference
        difference = abs(hour_angle - minute_angle)

        # Smaller angle
        return min(
            difference,
            360 - difference
        )