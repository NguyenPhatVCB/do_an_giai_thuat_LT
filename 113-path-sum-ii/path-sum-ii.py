# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum):

        res = []
        path = []

        def dfs(node, remain):

            if not node:
                return

            path.append(node.val)

            remain -= node.val

            if not node.left and not node.right and remain == 0:
                res.append(path[:])

            dfs(node.left, remain)
            dfs(node.right, remain)

            path.pop()

        dfs(root, targetSum)
        return res