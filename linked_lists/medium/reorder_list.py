"""

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # two pointers to find the middle node of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        second_half = slow.next
        slow.next = None
        prev_node = None
        while second_half:
            tmp = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = tmp
        
        # merge first half with second half
        first_half = head
        second_half = prev_node

        # while second halft is not None, because
        # for odd numbers, it will always be the case that this half is less in size
        while second_half:
            temp_head_1 = first_half.next
            temp_head_2 = second_half.next
            first_half.next = second_half
            second_half.next = temp_head_1
            second_half = temp_head_2
            first_half = temp_head_1

            

            



        


