# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution_iterative:
    def reverseList(self, head):
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre


class Solution_recursive:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, pre=None):
        if not node:
            return pre
        cur = node.next
        node.next = pre
        return self._reverse(cur, node)
