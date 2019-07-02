# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
     
        q = PriorityQueue()
        dummy = ListNode(None)

        for node in lists:
            cur = node
            while cur is not None:
                q.put(cur.val)
                cur = cur.next
        cur = dummy
        while not q.empty():
            cur.next = ListNode(q.get())
            cur = cur.next
      
        return dummy.next
