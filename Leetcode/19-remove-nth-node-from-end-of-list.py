# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 목록 끝에서부터 n 번째 노드를 제거해야함...
        
        lst = []
        node = head
        while node != None:
            lst.append(node.val)
            node = node.next
        length = len(lst)
        lst = lst[:length-n] + lst[length-n+1:]

        if len(lst) == 0:
            return None

        answer = ListNode(lst[0])
        node = answer
        for i in range(1, len(lst)):
            node.next = ListNode(lst[i])
            node = node.next

        return answer
