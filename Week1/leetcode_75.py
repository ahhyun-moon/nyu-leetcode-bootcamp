class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Thinking Process
        # Two pointers at the start and end of the list
        # ptr_0 points at available position for next 0
        # ptr_2 points at available position for next 2
        # Iterate through the list and swap the number: 
        # if curr num = 0, swap with the num at 0 ptr
        # if curr num = 2, swap with the num at 2 ptr
        ptr_0, curr = 0, 0
        ptr_2 = len(nums) - 1
        while curr <= ptr_2:
            if nums[curr] == 0:
                nums[curr], nums[ptr_0] = nums[ptr_0], nums[curr]
                ptr_0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[ptr_2] = nums[ptr_2], nums[curr]
                ptr_2 -= 1
            else:
                curr += 1
