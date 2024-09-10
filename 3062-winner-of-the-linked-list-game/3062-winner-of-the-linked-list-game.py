# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        curr = head.next
        even = 0
        odd = 0
        while curr:
            if curr.val > head.val:
                odd +=1
            else:
                even +=1
            if curr.next:
                curr = curr.next.next
            else:
                curr = curr.next
            head = head.next.next
            
        if odd > even:
            return "Odd"
        elif even > odd:
            return "Even"
        return "Tie"

        