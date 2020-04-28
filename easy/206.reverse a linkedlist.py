
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        n_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return n_node 