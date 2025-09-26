# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy= ListNode(0,head)
        l=dummy
        r=head

        while n>0:
            r=r.next
            n-=1

        while r:
            l=l.next
            r=r.next
        l.next=l.next.next
        return dummy.next

        