# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        cur = head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next

        if count % 2 == 0:
            mid = int(count/2)+1
        else:
            mid = int((count/2)+1)

        cur = head
        while (mid-1) != 0:
            cur = cur.next
            mid -= 1
        return cur
