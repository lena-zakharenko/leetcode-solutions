from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            if (target - value) in nums:
                if nums.index(target - value) != i:
                    return [i, nums.index(target - value)]