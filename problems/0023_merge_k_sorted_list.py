# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sorted_list_head = sorted_list_tail = ListNode(0)
        
        pq = PriorityQueue()
        
        def add_node_in_pq(idx, node):
            if node:
                pq.put((node.val, idx, node))
        
        for idx, node in enumerate(lists):
            add_node_in_pq(idx, node)
        
        while not pq.empty():
            _, idx, node = pq.get()
            add_node_in_pq(idx, node.next)
            node.next = None
            sorted_list_tail.next = node
            sorted_list_tail = sorted_list_tail.next
        
        return sorted_list_head.next
