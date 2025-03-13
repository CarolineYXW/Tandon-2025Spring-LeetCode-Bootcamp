# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        slow = head
        fast = head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            if fast.next is not None:
                fast = fast.next
        mid = slow.next
        prev = None
        cur = mid
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True