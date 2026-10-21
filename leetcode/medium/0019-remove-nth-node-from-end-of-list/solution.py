# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        if length == n:
            return head.next

        current = head

        for i in range(length - n - 1):
            current = current.next

        current.next = current.next.next

        return head

        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        