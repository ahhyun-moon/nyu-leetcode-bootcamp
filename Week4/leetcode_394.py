class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_token, cur_number =  '', 0
        
        for char in s:            
            if char == '[':
                stack.append( (cur_token, cur_number) )
                cur_token = ''
                cur_number = 0
            elif char == ']':
                prev_token, repeat_times = stack.pop()
                cur_token = prev_token + cur_token * repeat_times
            elif char.isdigit():
                cur_number = cur_number*10 + int(char)
            else:
                cur_token += char
        return cur_token