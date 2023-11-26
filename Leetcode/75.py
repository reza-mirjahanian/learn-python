class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k1 = -1
        # k2 = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == 0:
        #         if k1 != -1 and k1 < n:
        #             nums[k1], nums[i] = nums[i], nums[k1]
        #             k1 += 1
        #         if k2 < n:
        #             nums[k2], nums[i] = nums[i], nums[k2]
        #             k2 += 1
        #     elif nums[i] == 1:
        #         if k1 == -1:
        #             k1 = k2
        #         if k2 < n:
        #             nums[k2], nums[i] = nums[i], nums[k2]
        #             k2 += 1       
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


                # The Dutch National Flag algorithm, also known as 3-way partitioning, is an algorithm for sorting an array containing three distinct values. The algorithm was designed to solve the problem of sorting an array containing only 0s, 1s, and 2s, which is similar to the problem in the given question.