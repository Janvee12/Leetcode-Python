# Problem: Longest Substring Without Repeating Characters
# Platform: LeetCode
# Approach: Sliding Window + HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in current window
        st = set()
        
        # Left pointer of window
        l = 0
        
        # Variable to store maximum length
        max_len = 0

        # Right pointer iterates over string
        for r in range(len(s)):
            
            # If duplicate found, shrink window from left
            while s[r] in st:
                st.remove(s[l])
                l += 1

            # Add current character to set
            st.add(s[r])

            # Update maximum length
            max_len = max(max_len, r - l + 1)

        return max_len