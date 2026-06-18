# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        ptr = dummy
        second = dummy
        leng = 0
        # iterate until ptr is n steps away from head
        for _ in range(n + 1): 
            ptr = ptr.next
        
        while ptr: 
            ptr = ptr.next
            second = second.next 
        

        second.next = second.next.next

        return dummy.next
        