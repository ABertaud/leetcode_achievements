# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp_str = ""
        while head:
            tmp_str += str(head.val)
            head = head.next
        return tmp_str == tmp_str[::-1]