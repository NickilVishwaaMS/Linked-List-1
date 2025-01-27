#Time Complexity:O(n)
#Space Complexity:O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        curr=head
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev