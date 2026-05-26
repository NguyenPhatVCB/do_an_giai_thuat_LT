class Solution:
    def rotateRight(self, head, k):

        if not head or not head.next or k == 0:
            return head

        # Tìm độ dài
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Tạo vòng tròn
        tail.next = head

        # Số bước cần đi tới node mới
        k = k % length
        steps = length - k

        # Tìm node trước head mới
        current = head

        for _ in range(steps - 1):
            current = current.next

        # Head mới
        new_head = current.next

        # Cắt vòng tròn
        current.next = None

        return new_head