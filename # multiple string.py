```python id="multiply_strings_43" # ============================ # PLATFORM: # LeetCode # (43. Multiply Strings) # ============================

# ============================ # PROBLEM: # ============================ # # Given two non-negative integers # num1 and num2 represented as strings, # return their product as a string. # # Constraints: # - You cannot convert the whole string # directly into an integer. # # ============================ # APPROACH: # ============================ # # This simulates the manual multiplication # we do on paper. # # Key idea: # - Reverse both strings # - Multiply digit by digit # - Store results in an array # - Handle carry immediately # - Remove leading zeros # # ============================

class Solution:

def multiply(self, num1: str, num2: str) -> str:

# ============================ # EDGE CASE # ============================ if num1 == "0" or num2 == "0": return "0"

# result can have at most len1 + len2 digits res = [0] * (len(num1) + len(num2))

# reverse strings for easier indexing num1 = num1[::-1] num2 = num2[::-1]

# ============================ # MULTIPLY DIGITS # ============================ for i1 in range(len(num1)): for i2 in range(len(num2)):

digit = int(num1[i1]) * int(num2[i2])

# add to current position res[i1 + i2] += digit

# carry handling res[i1 + i2 + 1] += res[i1 + i2] // 10 res[i1 + i2] %= 10

# ============================ # REMOVE LEADING ZEROS # ============================ res = res[::-1]

start = 0 while start
