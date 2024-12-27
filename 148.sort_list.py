# https://leetcode.com/problems/sort-list/description/
# Given the head of a linked list, return the list after sorting it in ascending order.

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Topics
# Linked List
# Two Pointers
# Divide and Conquer
# Sorting
# Merge Sort

from typing import Optional
from utils import list_to_linked_list, ListNode


class Solution:
    def sortList(self, list1: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head

        li = []

        while list1:
            li.append({"node": list1, "val": list1.val})
            list1 = list1.next

        sorted_li = sorted(li, key=lambda key: key["val"])

        for x in sorted_li:
            tail.next = x["node"]
            tail = tail.next
            tail.next = None  # break recursion

        return head.next


s = Solution()
# print(s.sortList(list_to_linked_list([2, 2, 1, 3])))
print(s.sortList(list_to_linked_list([4, 19, 14, 5, -3, 1, 8, 5, 11, 15])))
