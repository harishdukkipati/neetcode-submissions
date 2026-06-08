# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Plan 
# we need to create a node called tail 
# set merge to tail
# go while list1 and list2 
# if l1.val <= l2.val
# merge.next = l1 
# l1 = l1.next
# else 
#merge.next = l1
# l2 = l2.next

# merge = merge.next
# if l1
# merge.next = l1
#if l2 
# merge.next = l2
# return tail.next 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        merge = tail 

        while list1 and list2:
            if list1.val <= list2.val:
                merge.next = list1 
                list1 = list1.next
            else:
                merge.next = list2
                list2 = list2.next
            merge = merge.next
        
        if list1:
            merge.next = list1
        
        if list2:
            merge.next = list2 
        
        return tail.next