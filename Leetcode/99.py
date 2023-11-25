# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # # in-order travers this tree
        # def inorder(node):
        #     if node:
        #         return inorder(node.left) + [node] + inorder(node.right)
        #     return []
        #
        # # get the in-order list of nodes
        # temp = inorder(root)
        # # sort all the values of the tree
        # sort = [n.val for n in temp]
        # sort.sort()
        #
        # # just copy all the value from sorted list
        # for i in range(len(sort)):
        #     temp[i].val = sort[i]

# We simply do an inorder traversal of BST and since we know inorder traversal moves to the nodes in ascending order.
# So, while doing the inorder traversal we check if the current value if less than the previous value which should not have been possible as inorder traversal should have been in ascending order thus there is a problem here.
# We save these nodes as first and second in separate variables so that we know that here was a problem.

        def dfs(root):
            if root is None:
                return
            # inside a dfs(), 'nonlocal' is must if 'prev' being modified
            nonlocal prev, first, second # it lets you assign values to a variable in an outer (but non-global) scope.
            dfs(root.left)
            if prev and prev.val > root.val:
                if first is None:
                    first = prev
                second = root
            prev = root
            dfs(root.right)

        prev = first = second = None
        dfs(root)
        first.val, second.val = second.val, first.val