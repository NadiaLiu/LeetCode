# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = 0
        v1,v2 = 0,0
        while l1 != None:
            v1 += pow(10,i)*l1.val
            l1 = l1.next
            i+= 1
        i = 0
        while l2 != None:
            v2 += pow(10,i)*l2.val
            l2 = l2.next
            i+= 1
        v3 = v1 + v2
        list3 = list(map(int, str(v3)))
        l3 = ListNode(0)
        head = l3
        for j in range(len(list3)-1,-1,-1):
            l3.next = ListNode(list3[j])
            l3 = l3.next
        return head.next