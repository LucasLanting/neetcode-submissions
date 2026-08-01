# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        curr1 = list1
        curr2 = list2
        while curr1:
            list.append(curr1.val)
            curr1 = curr1.next

        while curr2:
            list.append(curr2.val)
            curr2 = curr2.next
        
        list = sorted(list)
        
        listNodes = []
        for element in list:
            listNodes.append(ListNode(element, None))

        if listNodes:
            for i in range(len(listNodes)-1):
                listNodes[i].next = listNodes[i+1]
            return listNodes[0]
        else:
            return None
