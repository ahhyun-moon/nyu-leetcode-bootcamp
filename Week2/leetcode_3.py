class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force
        # Scan longest substring at every index using set

        # Optimized - Sliding Window with Dictionary storing last seen index
        left = 0
        max_len = 0
        seen = {}
        for right in range(len(s)):
            char = s[right]
            if char not in seen:
                max_len = max(max_len, right - left +1)
            else:
                if seen[char] < left:
                    max_len = max(max_len, right - left +1)
                else:
                    left = seen[char] + 1
            seen[char] = right
        return max_len
