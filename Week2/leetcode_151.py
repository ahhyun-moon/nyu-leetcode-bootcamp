from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        # Method 1) Split the string into words and reverse the word list
        # words = s.split()
        # words.reverse()
        # return (' '.join(words))
        
        # Method 2) deque - push new word in front of result deque
        result = deque()
        s = s.strip() # Remove leading/tailing spaces
        curr, end = 0, len(s)
        word = []
        while curr < end:
            # Append the word in front of the deque by inserting on left
            if s[curr] == ' ' and word:
                result.appendleft(''.join(word))
                word = []
            # Append the char into current word
            elif s[curr] != ' ':
                word.append(s[curr])
            curr += 1
        # Append the last word
        result.appendleft(''.join(word))
        # Return as a string joined with space 
        return ' '.join(result)        