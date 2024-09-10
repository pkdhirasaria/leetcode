# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                top = stack.pop()
                if stack:
                    prev = stack[-1]
                    prev.next = curr
                top.next = None
            stack.append(curr)
            curr = curr.next
        return stack[0]
