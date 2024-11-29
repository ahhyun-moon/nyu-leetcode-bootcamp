class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Thought process:
        # two equal subset sum means entire sum equals twice the subset sum
        # find from all combinations with sum goal (total sum / 2)
        total_sum = sum(nums)
        if total_sum % 2 != 0: return False
        sum_goal = total_sum // 2
        n = len(nums)
        # Brute Force:
        # def checkSum(endIdx, curr_sum):
        #     if curr_sum == 0:
        #         return True
        #     if n == 0 or curr_sum < 0:
        #         return False
        #     result = checkSum(endIdx - 1, curr_sum - nums[endIdx - 1]) or \
        #             checkSum(endIdx - 1, curr_sum)
        #     return result
        # return checkSum(n - 1, sum_goal)
        # 
        # DP Optimized:
        dp = [False] * (sum_goal + 1)
        dp[0] = True 
        for num in nums:
            for j in range(sum_goal, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[sum_goal]