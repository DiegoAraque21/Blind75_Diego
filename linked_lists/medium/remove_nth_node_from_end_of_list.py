"""

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Two pointers solution. Makes it O(n) time and 0(1) space complexity
# move left pointer as soon as the distance between left and right is bigger tha n
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy node at the beginning
        dummy = ListNode()
        dummy.next = head

        # two pointers
        i = j = dummy
        counter = 0
        # advance both pointers
        # left one starts to advance, when the difference between
        # right and left is greater than n
        while j:
            if counter > n:
                i = i.next
            j = j.next
            counter += 1
        
        # if the linked list has only one value
        # return None
        if counter == 2:
            return None
        # if you need to eliminate the last node
        # make the next of node i, j
        # j will always be null
        elif n == 1:
            i.next = j
        # if you need to eliminate another element
        # just set it to the .next.next 
        else:
            i.next = i.next.next

        return dummy.next

# Array solution. O(n) time complexity and O(1) space complexity
# Iterate once through the linked list and represent it as an array of Nodes
# Since the array is indexed we will just have to acces the node len(arr) - n
# and delete it

# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         # save the head to return later
#         list1 = head
#         # array filled with all nodes,
#         # we will be able to index it and only pass through the array once
#         arr =[]

#         # while the ehad is not none
#         # add nodes to the list
#         while head:
#             arr.append(head)
#             head = head.next

#         # if the linked list has one value or was empty
#         # always return None
#         if len(arr) <= 1:
#             return None
#         else:
#             # if the value we have to remove is bigger the last one
#             if len(arr) - n + 1 == len(arr):
#                 arr[len(arr) - n - 1].next = None
#             # if the value is the first one
#             elif len(arr) - n - 1 < 0:
#                 return list1.next
#             # if the value is on every other position of the linked list
#             else:
#                 arr[len(arr) - n - 1].next = arr[len(arr) - n + 1]
#             return list1