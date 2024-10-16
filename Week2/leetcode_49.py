from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            sorted_w = tuple(sorted(word))
            if sorted_w not in words:
                words[sorted_w] = []
            words[sorted_w].append(word)
        return words.values()