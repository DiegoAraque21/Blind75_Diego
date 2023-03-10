"""

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # slow pointer
        slow_ptr = head
        # fast pointer
        fast_ptr = head

        # while there is no None
        while fast_ptr and fast_ptr.next:
            # shift slow by 1
            slow_ptr = slow_ptr.next
            # shift fast by 2
            fast_ptr = fast_ptr.next.next

            # if they meet, a cycle exists
            if fast_ptr == slow_ptr:
                return True

            
        return False