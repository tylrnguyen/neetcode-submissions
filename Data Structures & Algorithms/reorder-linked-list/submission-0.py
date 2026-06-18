# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find middle point of list 
        # 2. reverse second half of list 
        # 3. start pointers on opposite ends, make new list

        if not head.next or not head.next.next: 
            return

        # 1
        slow = head
        fast = head

        while fast.next and fast.next.next: 
            slow = slow.next
            fast = fast.next.next
        
        p2 = slow.next
        slow.next = None
        p1 = head

        # 2
        prev = None
        while p2 and p2.next: 
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp
        p2.next = prev

         # 3
        while p1 and p2: 
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next

