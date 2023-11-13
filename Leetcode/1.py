from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        # for i in range(len(nums)):
        #     t = target - nums[i]
        #     if t in d.keys():
        #         return [d[t], i]
        #     d[nums[i]] = i

        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i