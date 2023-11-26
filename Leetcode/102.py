# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # result = []
        # count = 0

        # def level(count , root):
        #     if root == None :
        #         return 

        #     if len(result) <= count:
        #         result.append([])    
            
        #     result[count].append(root.val)
        #     count += 1
        #     level(count , root.left)
        #     level(count , root.right) 

        # level(count , root)
        # return result 

        result = []
        q = collections.deque()
        q.append(root)
        
        while q:
            n = len(q)
            level = []

            for i in range(n):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                result.append(level)    

        
        return result       