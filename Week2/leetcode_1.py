class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_i = {}
        ans = []
        for i, num in enumerate(nums):
            if (target - num) in num_i:
                return [i, num_i[target - num]]
            num_i[num] = i
