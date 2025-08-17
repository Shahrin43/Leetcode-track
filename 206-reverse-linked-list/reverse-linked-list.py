# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        stack = []
        curr = head
        
        # Push all nodes into the stack
        while curr:
            stack.append(curr)
            curr = curr.next
        
        # Pop nodes and rebuild reversed list
        new_head = stack.pop()
        curr = new_head
        
        while stack:
            node = stack.pop()
            curr.next = node
            curr = node
        
        # Last node should point to None
        curr.next = None
        return new_head

                
                
            