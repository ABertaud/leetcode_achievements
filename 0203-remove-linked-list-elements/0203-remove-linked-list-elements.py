# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        dummy = head
        while dummy.next:
            if dummy.next.val == val:
                if dummy.next.next:
                    dummy.next = dummy.next.next
                else:
                    dummy.next = None
                    return head
            else:
                dummy = dummy.next
        return head
                

