class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # fast đi trước n bước
        for _ in range(n):
            fast = fast.next
        
        # di chuyển cả hai
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # xóa node
        slow.next = slow.next.next
        
        return dummy.next