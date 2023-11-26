        # def backtrack(i, curr):
        #     if i == len(nums):
        #         return

        #     for j in range(i, len(nums)):
        #         curr.append(nums[j])
        #         res.append(curr[:])
        #         backtrack(j + 1, curr)
        #         curr.pop()

        # res = [[]]
        # backtrack(0, [])
        # return res        
        list1 = [[]]
        n=len(nums)
        for i in range(1,2**n):
            list2=[]
            for j in range(n):
                if (i&1<<j):
                    list2.append(nums[j])
            list1.append(list2)
        return list1        