# ============================
# PLATFORM:
# LeetCode
# (Earliest Finish Time)
# ============================

# ============================
# IDEA
# ============================
#
# We must complete:
#
# - One land ride
# - One water ride
#
# in any order.
#
# Instead of checking every
# pair of rides O(n*m),
# this solution computes:
#
# Land -> Water
# Water -> Land
#
# separately and returns
# the minimum answer.
#
# ============================

from math import inf
from typing import List

class Solution:

    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def check(
            start1,
            duration1,
            start2,
            duration2
        ):

            # ====================
            # Earliest finish time
            # among first rides
            # ====================

            first_finish = inf

            for i in range(len(start1)):

                first_finish = min(
                    first_finish,
                    start1[i] + duration1[i]
                )

            # ====================
            # Complete second ride
            # after first ride
            # ====================

            answer = inf

            for i in range(len(start2)):

                finish_time = (
                    max(
                        first_finish,
                        start2[i]
                    )
                    + duration2[i]
                )

                answer = min(
                    answer,
                    finish_time
                )

            return answer

        # ========================
        # Land -> Water
        # ========================

        land_then_water = check(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        # ========================
        # Water -> Land
        # ========================

        water_then_land = check(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(
            land_then_water,
            water_then_land
        )