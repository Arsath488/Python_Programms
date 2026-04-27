

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        curr = head
        for _ in range(k):
            if not curr:
                return head 
            curr = curr.next
        
   
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
       
        head.next = self.reverseKGroup(curr, k)
        
      
        return prev
