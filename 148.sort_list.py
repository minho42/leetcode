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
    # using builtin sort
    def sortList1(self, list1: Optional[ListNode]) -> Optional[ListNode]:
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

    # using merge sort myself
    def sortList2(self, list1: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not list1 or not list1.next:
            return list1

        n = 0
        temp = list1
        while temp:
            temp = temp.next
            n += 1

        m = n // 2
        left = list1
        prev = None
        for i in range(m):
            prev = list1
            list1 = list1.next
        prev.next = None
        right = list1

        left = self.sortList2(left)
        right = self.sortList2(right)
        return self.merge(left, right)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        head = ListNode()
        tail = head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return head.next

    # ref: https://youtu.be/TGveA1oFhrc?si=hJ-E5B9l19MWfkCM
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head

        left = head
        # neetcode used temp but temp is not requied here
        mid = self.getMid(head)
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    # ref: https://youtu.be/TGveA1oFhrc?si=hJ-E5B9l19MWfkCM
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


s = Solution()
# print(s.sortList([]))
# print(s.sortList(list_to_linked_list([2, 1])))
# print(s.sortList(list_to_linked_list([3, 2, 1])))
# print(s.sortList(list_to_linked_list([2, 2, 1, 3])))
print(s.sortList(list_to_linked_list([4, 19, 14, 5, -3, 1, 8, 5, 11, 15])))
