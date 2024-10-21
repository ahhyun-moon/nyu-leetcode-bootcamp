# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Optimized: 
        # Thought Process:
        # Move fast pointer to nth position (slow ptr (start) + n = fast pointer)
        # Move both fast and slow pointers until the fast pointer reaches the end
        # Slow pointer will be at the previous node of nth pointer (fast ptr (end) - n = slow ptr)
        slow_ptr,fast_ptr = head, head
        for _ in range(n):
            fast_ptr = fast_ptr.next
        if fast_ptr is None:
            return head.next
        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return head
    
    
    # Initial Approach:
    #     # Thought Process:
    #     # Reverse the list and scan from the start of the reversed list for nth element
    #     # Remove the nth element and reverse back the list
    #     ptr = head
    #     reversed_ptr = self.reverseLL(head)
    #     i = 1
    #     curr_ptr = reversed_ptr
    #     if n == 1:
    #         removed_ptr = self.reverseLL(reversed_ptr.next)
    #     else:
    #         while curr_ptr and curr_ptr.next is not None:
    #             if i + 1 == n:
    #                 curr_ptr.next = curr_ptr.next.next
    #                 curr_ptr = curr_ptr.next
    #             else:
    #                 curr_ptr = curr_ptr.next
    #             i += 1
    #         removed_ptr = self.reverseLL(reversed_ptr)
    #     return removed_ptr

    # def reverseLL(self, head):
    #     ptr = head
    #     prev_ptr = None
    #     while ptr is not None:
    #         next_ptr = ptr.next
    #         ptr.next = prev_ptr
    #         prev_ptr = ptr
    #         ptr = next_ptr
    #     return prev_ptr