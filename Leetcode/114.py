# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getStack(self,root,st) :
        if root is None :
            return

        self.getStack(root.right,st)
        self.getStack(root.left,st)
        st.append(root)
        return st

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None :
            return 

        head = cur = TreeNode(-1)
        st = self.getStack(root,[])

        for i in range(len(st)) :
            cur.left = None
            cur.right = st.pop()
            cur = cur.right
        return head.right        