class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Thinking Process:
        # Two pointers start at begining and end of the height list
        start_ptr = 0
        end_ptr = len(height) - 1
        max_area = 0
        # Scan until they meet in the middle  (n)
        while start_ptr < end_ptr:
            # Area of water will be:
            #    min(two max heights at each end) * (end index - start index)
            area = min(height[start_ptr], height[end_ptr]) * (end_ptr - start_ptr) 
            max_area = max(max_area, area)
            # Move the pointer that has lower height
            if height[start_ptr] < height[end_ptr]:
                start_ptr += 1
            else:
                end_ptr -= 1
        return max_area