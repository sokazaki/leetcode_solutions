# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        stack1, stack2 = [], []
        cur = l1
        while cur:
            stack1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            stack2.append(cur.val)
            cur = cur.next
        
        res, total = None, 0
        while len(stack1) > 0 or len(stack2) > 0:
            if len(stack1) > 0:
                total += stack1.pop()
            if len(stack2) > 0:
                total += stack2.pop()
            
            n = ListNode(total % 10)
            n.next, res = res, n
            total = total//10
        
        if total > 0:
            n = ListNode(total)
            n.next, res = res, n
        
        return res 
