class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1 
        result = 0
        curr= 0
        MIN = -2**31
        MAX = 2**31 - 1
        # Strip the leading/tailing spaces and get correct end index
        s = s.strip()
        end = len(s) 
        # Return 0 if empty string
        if len(s) == 0:
            return 0
        # Update the sign (neg/pos) based on the first char
        if s[curr] == '-':
            sign = -1 
            curr += 1
        elif s[curr] == '+':
            curr += 1
        # Scan through the string 
        # We CANNOT add another digit when:
        #   1. Current result is already greater than 2^31 // 10 
        #   2. Current result eqaul 2^31 // 10 and the digit we're trying to add is greater than 8
        # If possible to add: 
        #   Shift the current result by multiplying 10 and add current digit
        #   Add 1 to the index to scan next in string
        while curr < end:
            if s[curr].isdigit():
                if (result > MAX // 10) or (result == MAX // 10 and int(s[curr]) > MAX % 10):
                    return MAX if sign == 1 else MIN
                result = 10 * result + int(s[curr])
                curr += 1
            else:
                break
        # Return the result by multiplying the sign (-1 or 1)
        return result * sign
    