class Solution:
    def deleteDuplicates(self, head):
        
        current = head

        while current and current.next:

            # Nếu trùng
            if current.val == current.next.val:
                current.next = current.next.next

            # Không trùng
            else:
                current = current.next

        return head