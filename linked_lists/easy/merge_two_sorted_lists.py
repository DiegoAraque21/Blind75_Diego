"""

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        node = ListNode()
        head = node

        while list1 or list2:
            # if one of the lists has been completely traversed
            if list1 == None:
                head.next = list2
                break
            elif list2 == None:
                head.next = list1
                break
            # if the val in l1 is less, insert it
            elif list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            # insert value of l2
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        return node.next

