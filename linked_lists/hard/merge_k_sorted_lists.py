"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # edge cases
        if len(lists) == 0 or lists == None:
            return None

        # Iterate through the lists array
        # until it has one element. We are dividing by 2 in each
        # iteration, so that we don't go through k in every step.
        # but just log(k)
        while len(lists) > 1:
            result = []
            # for increments by 2, to get 2 lists per iteration
            # if it is an odd length we do a check, if not in range, list2 is None
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = None
                if i + 1 < len(lists):
                    list2 = lists[i+1]
                # merge lists
                result.append(self.merge2Lists(list1, list2))
            # we divided for example the first 4 linked lists into 2, and then into 1.
            lists = result
        
        # since it only has one value, we return the first element
        return lists[0]
        
    def merge2Lists(self, list1, list2):
        # empty onde at the beginning, to keep tack of the one we are returning
        empty_node = ListNode()
        tail_node = empty_node
                
        # while they both of them are not empty
        while list1 or list2:
            # list1 is empty, do necessary changes and return
            if not list1:
                tail_node.next = list2
                return empty_node.next
            # list 2 is empty, do necessary changes
            elif not list2:
                tail_node.next = list1
                return empty_node.next
            # add list1 value to the end of the list
            # and update list1
            elif list1.val < list2.val:
                tail_node.next = list1
                list1 = list1.next
            # add list2 value to the end of the list
            # and update list2
            else:
                tail_node.next = list2
                list2 = list2.next
            tail_node = tail_node.next