# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Thought Process:
        # Brute Force: O(n) TC and O(n) Space
        # Copy the LL to a list and compare if reversed list is equal to the original list
        # ll_list = []
        # while head is not None:
        #     ll_list.append(head.val)
        #     head = head.next
        # return ll_list == ll_list[::-1]

        # Optimized: O(n) TC and O(1) Space
        # Reverse the second half of the LL and compare LL from start and 2nd half start
        first_start = head
        second_start = self.getSecondStart(head)
        reversed_start = self.reverseLL(second_start)
        while first_start is not None and reversed_start is not None:
            if first_start.val != reversed_start.val:
                return False
            first_start = first_start.next
            reversed_start = reversed_start.next
        return True

    def reverseLL(self, head):
        ptr = head
        prev_ptr = None
        while ptr is not None:
            next_ptr = ptr.next
            ptr.next = prev_ptr
            prev_ptr = ptr
            ptr = next_ptr
        return prev_ptr

    def getSecondStart(self, head):
        slow_ptr = head
        fast_ptr = head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr