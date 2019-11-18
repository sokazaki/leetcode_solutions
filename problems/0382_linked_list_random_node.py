# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head):
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self):
        pointer = self.head
        index = random.randint(0, self.length-1)
        for i in range(index):
            pointer = pointer.next
        return pointer.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
