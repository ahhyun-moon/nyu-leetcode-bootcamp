class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Thinking Process:
        # Prepare a result list size of nums list
        # Product for each num at i will be:
        # (prefix product until i - 1) * (postfix product from i + 1)
        # Accumulate the prefix product as we iterate from start
        # Store the prefix product at result[i]
        # Accumulate the postfix product as we iterate the num list from end
        # Multiply the accumulated postfix product to the stored prefix product at result[i]
        n = len(nums)
        result = [0] * n
        prefix_product = 1
        postfix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= postfix_product
            postfix_product *= nums[i]
        return result
