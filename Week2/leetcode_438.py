from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Brute Force: Check at every index 
        # whether current substring has same count of chars in p
        # length = len(p)
        # result = []
        # p_counts = Counter(p)
        # for i in range(len(s) - length + 1):
        #     if Counter(s[i:i + length]) == p_counts:
        #         result.append(i)
        # return result
        # Sliding Window: Remove and Add character in hash map
        # while scanning through the string
        len_p, len_s = len(p), len(s)
        result = []
        p_count = Counter(p)
        s_count = Counter()
        for i in range(len_s):
            # Add 1 to the current char in counter
            s_count[s[i]] += 1
            # If current index is larger than the length of p,
            # Remove the count of left most char in the s_counter
            if i >= len_p:
                if s_count[s[i - len_p]] == 1:
                    del s_count[s[i - len_p]]
                else:
                    s_count[s[i - len_p]] -= 1
            # Check if current window and p have the same count of chars
            if s_count == p_count:
                result.append(i - len_p + 1)
        return result