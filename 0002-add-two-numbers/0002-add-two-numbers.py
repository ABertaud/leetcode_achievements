#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        total = head
        retained = False
        i = 0
        while l1 or l2:
            tmp_nb = 0
            if l1:
                tmp_nb += l1.val
                l1 = l1.next
            if l2:
                tmp_nb += l2.val
                l2 = l2.next
            if retained == True:
                tmp_nb += 1
                retained = False
            if tmp_nb >= 10:
                tmp_nb -= 10
                retained = True
            if i == 0:
                total.val = tmp_nb
            else:
                total.next = ListNode(tmp_nb)
                total = total.next
            i += 1
        if retained == True:
             total.next = ListNode(1)
        return head