# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):

        if n == 0:
            return []

        def build(l, r):

            if l > r:
                return [None]

            res = []

            for root in range(l, r + 1):

                left_trees = build(l, root - 1)
                right_trees = build(root + 1, r)

                for left in left_trees:
                    for right in right_trees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        res.append(node)

            return res

        return build(1, n)