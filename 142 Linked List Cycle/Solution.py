# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        """
		The idea behind getting the start of the loop is same follows the same logic as finding the loop.

		We have to pointers and fast and slow and we know that if there is a cycle they will collide.

		How do we find the start of the loop ?

		Let's say slow travelled k nodes before entering the loop.
		So fast travelled total of 2k nodes in the mean time and out of those 2k nodes , k nodes were outside the loop
		So fast travelled k nodes in the loop. As k can be large we define K = k % loop_size from the start of the loop.

		We now have following facts:
		1 - slow travelled k nodes and is at start of the loop.
		2 - fast travelled 2k nodes and is at K nodes from the start of the loop.

		From fact 2, we can say that fast is also loop_size - k nodes from the start of the loop or loop_size - k nodes behind
		slow.

		Given that fast is catching up to slow at 1 node per iteration, they will collide after loop_size - k iterations or loop_size - k
		nodes from the start.

		Since the collision spot is loop_size - k from the start of the loop, it is also k nodes behind the start of the loop.

		So if we have a pointer at head and a pointer at Collision spot( both are k nodes away from the start of the loop),
		making them travel at 1 node at a time they will intersect at start of the loop after k iterations.
        """

        slow = head
        fast = head
        
        intersect = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersect = slow
                break
        
        if not intersect:
            return None
        
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow