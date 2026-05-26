# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head):

        def find_middle(start):
            prev = None
            slow = start
            fast = start

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None

            return slow

        def build(start):

            if not start:
                return None

            mid = find_middle(start)

            root = TreeNode(mid.val)

            if start == mid:
                return root

            root.left = build(start)
            root.right = build(mid.next)

            return root

        return build(head)