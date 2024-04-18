# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        cur = head
        
        while cur:
            length += 1
            cur = cur.next
         
        res = head
        for i in range(0, int(length / 2)):
            res = res.next
            
        return res