# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        dummy = node = ListNode(0)
        dummy.next = head

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            node.next = tmp
            head = head.next
            node = tmp.next

        return dummy.next
