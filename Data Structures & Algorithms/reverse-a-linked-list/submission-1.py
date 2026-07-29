# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:

            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev


node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)

newHead = Solution().reverseList(head)

current = newHead

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")