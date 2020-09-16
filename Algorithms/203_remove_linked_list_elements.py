# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return None


        while head.val == val:
            if head.next is None:
                return None
            head = head.next

        cur = head
        sign = 0
        while sign == 0 and cur is not None:
            if cur is None:
                return cur

            if cur.val == val:
                if cur.next is None:
                    return None
                else:
                    while cur.val == val:
                        head = head.next
                        cur  = head

            while cur.next is not None:
                if cur.next.val == val:
                    break
                cur = cur.next
            if cur.next is None:
                if cur.val != val:
                    sign = 1
            else:
                cur.next = cur.next.next
        return head
