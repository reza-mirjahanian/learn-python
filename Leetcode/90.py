class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        output = set()

        nums = sorted(nums)

        def backtrack(subset, index):
            output.add(subset)

            for i in range(index, N):
                backtrack(tuple(list(subset) + [nums[i]]), i + 1)

        backtrack(tuple(), 0)
        return output        