# https://leetcode.com/problems/merge-two-sorted-lists/


# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


from typing import Optional


# Topics
# Linked List
# Recursion


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}->{self.next}"

    def __iter__(self):
        cur = self
        while cur:
            yield cur.val
            cur = cur.next

    def to_list(self):
        return list(self)


def list_to_linked_list(li):
    # print(list_to_linked_list([1,2,3])) => 1->2->3->None
    next = None
    for x in li[::-1]:
        cur = ListNode(x, next)
        next = cur
    return cur


# ref: https://youtu.be/XIdigk956u0?si=58wdNnBsgLkK3Vgn


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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


s = Solution()
print(s.mergeTwoLists(list_to_linked_list([1, 2, 4]), list_to_linked_list([1, 3, 4])))
