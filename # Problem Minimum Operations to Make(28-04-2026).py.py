# Problem: Minimum Operations to Make a Uni-Value Grid
# Platform: LeetCode
# Approach: Flatten + Median
# Time Complexity: O(m*n log(m*n))
# Space Complexity: O(m*n)

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        # Step 1: Flatten the 2D grid into a 1D list
        # Flatten means converting something like:
        # grid = [[1, 2], [3, 4]]
        # into:
        # arr = [1, 2, 3, 4]
        # We do this because we want to treat all values together
        # (median can only be easily found in a 1D list)

        arr = []
        for row in grid:        # row = [1, 2] then [3, 4]
            for val in row:     # val = 1, 2, 3, 4
                arr.append(val)  # add each element into arr
        
        # Now arr contains all elements of grid in a single list

        # Step 2: Check if transformation is possible
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1
        
        # Step 3: Sort the flattened array
        arr.sort()

        # Step 4: Find median (middle element)
        median = arr[len(arr)//2]

        # Step 5: Calculate operations needed
        operations = 0
        for num in arr:
            operations += abs(num - median) // x
        
        return operations