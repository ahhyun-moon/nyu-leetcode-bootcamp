class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Thinking Process:
        # Use two pointers at the start and end of the list
        # If the sum of current pointers is less than the target,
        # Move the left pointer to the right.
        # If the sum is greater than the target, 
        # Move the right pointer to the left.
        # Continue searching until found.
        start_ptr, end_ptr = 0, len(numbers) - 1
        while start_ptr < end_ptr:
            curr_sum = numbers[start_ptr] + numbers[end_ptr]
            if curr_sum == target:
                return [start_ptr + 1, end_ptr + 1]
            elif curr_sum < target:
                start_ptr += 1
            else:
                end_ptr -= 1
