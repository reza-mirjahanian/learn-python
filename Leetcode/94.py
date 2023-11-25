# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else []

        def inorder(root):
            return  inorder(root.left) + [root.val] + inorder(root.right) if root else []

        def postorder(root):
            return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return inorder(root)    