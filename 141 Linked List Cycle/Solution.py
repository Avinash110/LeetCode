class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        """
        The idea behind finding cycle in linked list is using 2 pointers: 1 - Slow, 2 - Fast
        Slow moves at one node per iteration while Fast moves at two nodes per iteration.

        If they are in a cycle they are bound to collide, Why ? 
        Since Fast is moving at away from Slow at a rate of one node per iteration; it is also moving closer at a rate of
        one node per iteration.
        So there will be a time when Fast will be 1 node or 2 nodes away from Slow.
		Case 1:	 1-2-3-4
		           F S
        If fast is 1 node away from slow then they will collide in the next iteration since both of them will be at 4.
              
        Case 2:  1-2-3-4-5
                 F   S
		If fast is 2 nodes away from slow then they will collide after 2 iteration since both of them will be at 5.

		So they are bound to collide.

		We can also reason in this way that since they are in a cycle fast might hop over slow at some time so
		fast is at (i+1)th node and slow is at (i)th node i.e. in the previous iteration they both are bound to be at (i-1)th
		iteration. So they collied in the previous iteration.

		If fast reaches the end there is no cycle.
        """

        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False