# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_linked_list(l):    
    while True:
        print(l.val)
        if not l.next: 
            break
        l = l.next

def convert_linked_list_to_array(l):
    r = []
    while True:
        r.append(l.val)
        if not l.next:
            break
        l = l.next        
    return r

def convert_to_node_reverse(n):
    # 807 -> ListNode[7->0->8] -> return ListNode[7]
    prev = None
    for n in list(str(n)):
        cur = ListNode(int(n), prev)
        prev = cur
    return cur
    
def add_two_numbers(l1, l2):
    # [1,2,3] -> '123'
    a = "".join(map(str, convert_linked_list_to_array(l1)))
    b = "".join(map(str, convert_linked_list_to_array(l2)))
    total = int(a[::-1]) + int(b[::-1])
    return convert_to_node_reverse(total)
    
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Explanation: 342 + 465 = 807
# Output: [7,0,8]: LinkedNode[7]->...

l1 = [2,4,9]
l2 = [5,6,4,9]
a = ListNode(9)
b = ListNode(4, a)
c = ListNode(2, b)

d = ListNode(9)
e = ListNode(4, d)
f = ListNode(6, e)
g = ListNode(5, f)

r = add_two_numbers(c, g)
print(r)