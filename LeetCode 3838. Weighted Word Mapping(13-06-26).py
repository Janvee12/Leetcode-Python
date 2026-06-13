from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = sum(weights[ord(ch) - ord('a')] for ch in word)
            rem = total % 26

            # 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            ans.append(chr(ord('z') - rem))

        return ''.join(ans)
