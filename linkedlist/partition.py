# Medium

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:


# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]
 

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1 = None
        p2 = None
        p1_tail = None
        p2_tail = None
        if head == None:
            return head
        while head:
            if head.val < x:
                if p1 == None:
                    p1 = ListNode(head.val, None)
                    p1_tail = p1
                else:
                    p1_tail.next = ListNode(head.val, None)
                    p1_tail = p1_tail.next
                
            else:
                if p2 == None:
                    p2 = ListNode(head.val, None)
                    p2_tail = p2
                else:
                    p2_tail.next = ListNode(head.val, None)
                    p2_tail = p2_tail.next
                
            head = head.next
        if p2 != None and p1_tail != None: 
            p1_tail.next = p2
            return p1
        elif p2 != None:
            return p2
        else: 
            return p1
        
    def partition_improved(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less_tail = less_dummy
        greater_tail = greater_dummy

        curr = head

        while curr:
            if curr.val < x:
                less_tail.next = curr
                less_tail = less_tail.next
            else:
                greater_tail.next = curr
                greater_tail = greater_tail.next

            curr = curr.next

        # Important: terminate second list
        greater_tail.next = None

        # Connect both lists
        less_tail.next = greater_dummy.next

        return less_dummy.next