# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return

        q = deque()
        ans, ltr = [[root.val]], False
        q.append([root])
        while q:
            level = q.popleft()
            children, children_vals = [], []
            for node in level:
                if ltr:
                    if node.left:
                        children.append(node.left)
                        children_vals.append(node.left.val)
                    if node.right:
                        children.append(node.right)
                        children_vals.append(node.right.val)
                else:
                    if node.right:
                        children.append(node.right)
                        children_vals.append(node.right.val)
                    if node.left:
                        children.append(node.left)
                        children_vals.append(node.left.val)
            if children: q.append(reversed(children))
            if children_vals: ans.append(children_vals)
            if ltr: ltr = False
            else: ltr = True

        return ans        