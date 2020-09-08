class ListNode(object):
    def __init__(self, val=0, next=None)):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self,l1, l2):
        if l1 is None and l2 is None:
            return ListNode().next
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
           
            l1_node = 1
            n = 0
            while n == 0:
                execute_str = 'l1'+'.next'*l1_node+' is not None'
                if eval(execute_str):
                    l1_node += 1
                else:
                    n += 1

            l2_node = 1
            n = 0
            while n == 0:
                execute_str = 'l2' + '.next' * l2_node + ' is not None'
                if eval(execute_str):
                    l2_node += 1
                else:
                    n += 1


            l1_array = [eval('l1' + '.next' * nodes + '.val') for nodes in range(l1_node)]
            l2_array = [eval('l2' + '.next' * nodes + '.val') for nodes in range(l2_node)]
            n1 = 0
            n2 = 0
            linkList = []
            while n1 < l1_node and n2 < l2_node:
                if l1_array[n1] < l2_array[n2]:
                    linkList.append(l1_array[n1])
                    n1 += 1
                else:
                    linkList.append(l2_array[n2])
                    n2 += 1

            if n1 == l1_node:
                linkList.extend(l2_array[n2:])
            else:
                linkList.extend(l1_array[n1:])


            start_node = ListNode(-1)
            dummy = start_node
            for i in range(len(linkList)):
                new_node = ListNode(linkList[i])
                if i == 0:
                    dummy.val = new_node.val
                else:
                    while dummy.next is not None:
                        dummy = dummy.next
                    dummy.next = new_node

            return start_node
