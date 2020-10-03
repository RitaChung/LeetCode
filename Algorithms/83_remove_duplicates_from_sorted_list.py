# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        else:
            box = []
            cur = head
            prev = None
            while cur is not None:
                if cur.val in box:
                    prev.next = cur.next
                    cur = cur.next
                else:
                    box.append(cur.val)
                    prev = cur
                    cur = cur.next
            return head
