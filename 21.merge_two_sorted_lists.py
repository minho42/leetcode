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
