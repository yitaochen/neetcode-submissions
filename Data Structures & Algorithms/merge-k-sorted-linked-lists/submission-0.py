# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        k = len(lists)
        
        while True:
            index = -1
            for i in range(k):
                if not lists[i]:
                    continue
                if index == -1 or lists[index].val > lists[i].val:
                    index = i
            
            if index == -1:
                break 
            
            cur.next = lists[index]
            lists[index] = lists[index].next
            cur = cur.next
        
        return dummy.next
