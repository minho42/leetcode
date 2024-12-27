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
