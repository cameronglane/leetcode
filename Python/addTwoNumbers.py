# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = 0
        head = l1
        
        while l2:
            sum = l2.val + l1.val + temp
            l1.val = sum % 10
            temp = sum // 10
            if l1.next is None:
                l1.next = l2.next
                break
            if l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next
            
        while temp > 0:
            if l1.next is None:
                l1.next = ListNode(0)
            l1 = l1.next
            sum = l1.val + temp
            l1.val = sum % 10
            temp = sum // 10
            
        return head