"""

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # previous node
        prev_node = None
        # current node
        curr_node = head
        while curr_node:
            # temp variable for the next node
            # since we are changing it below
            temp_next = curr_node.next
            # change to which value it points
            curr_node.next = prev_node
            # change the previous node
            # so we can advanced through the linked list
            prev_node = curr_node
            # change the current one, for the same effect
            curr_node = temp_next
        
        return prev_node