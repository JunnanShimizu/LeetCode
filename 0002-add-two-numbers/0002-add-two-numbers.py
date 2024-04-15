# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        res = dummy
        car = 0

        while l1 or l2 or car:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + car

            if val >= 10:
                car = 1
                res.next = ListNode(val % 10)
            else:
                res.next = ListNode(val)
                car = 0

            res = res.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return dummy.next