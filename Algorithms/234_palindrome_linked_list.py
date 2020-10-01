# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        cur = head
        stack = []
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
        while len(stack) > 1:
            if stack.pop(0) != stack.pop():
                return False
        return True
