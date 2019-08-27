# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        l1, l2 = 0, 0
        cur1, cur2 = headA, headB

        while cur1:
            l1 += 1
            cur1 = cur1.next
        while cur2:
            l2 += 1
            cur2 = cur2.next

        if l1 < l2:
            headA, headB = headB, headA
            l1, l2 = l2, l1
        for _ in range(l1-l2):
            headA = headA.next

        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
