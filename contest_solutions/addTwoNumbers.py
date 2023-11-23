# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # A linked list Node is simply a class which has:
        #   - a value
        #   - a pointer to the next node in the list
        # We are trying to add 2 numbers one digit at the time, starting from left to right.
        rem = 0
        first = None
        curr = None
        while l1 is not None or l2 is not None or rem == 1:
            l1val = l1.val if l1 is not None else 0
            l2val = l2.val if l2 is not None else 0
            v = l1val + l2val + rem
            if v >= 10:
                # If more than 10, carry 1 over
                v -= 10
                rem = 1
            else:
                # in case from last time
                rem = 0
            
            if curr == None:
                curr = ListNode(v) # first node instance, with value v and next=None
                first = curr # Remember the first node, to return
            else:
                node = ListNode(v) # new node instance, with value v and next=None
                curr.next = node # set the current node.
                curr = node # move the current node to the new node.
            
            # If we haven't reached the end of the first number, move to the next digit
            if l1 is not None:
                l1 = l1.next
                
            # If we haven't reached the end of the second number, move to the next digit
            if l2 is not None:
                l2 = l2.next
        
        # Return the first node in our new number (the head of the list)
        return first
        
        
        