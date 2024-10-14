class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # Brute force
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         if curr_sum > max_sum:
        #             max_sum = curr_sum
        # return max_sum
        # Thinking Process
        # Store prefix sum as we scan through the list
        # If accumulated sum is less than the current number, 
        # Replace the max sum with the current number and start the prefix sum at curr num
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(curr_sum, max_sum)
        return max_sum