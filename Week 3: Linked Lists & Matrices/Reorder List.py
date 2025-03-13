# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        prev = None
        cur = mid
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head2 = head
        while prev and head2:
           temp = head2.next
           head2.next = prev
           prev = prev.next
           head2.next.next = temp
           head2 = temp