class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            # hoán đổi
            prev.next = second
            first.next = second.next
            second.next = first
            
            # di chuyển con trỏ
            prev = first
            head = first.next
        
        return dummy.next