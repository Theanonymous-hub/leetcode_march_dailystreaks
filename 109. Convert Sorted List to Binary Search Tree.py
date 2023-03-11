class Solution:
    def constructBST(self, leftHead: ListNode, rightHead: ListNode) -> TreeNode:
        if leftHead == rightHead:
            return None
        slow, fast = leftHead, leftHead
        while fast != rightHead and fast.next != rightHead:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.constructBST(leftHead, slow)
        root.right = self.constructBST(slow.next, rightHead)
        return root
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            root = TreeNode(head.val)
            return root
        return self.constructBST(head, None)
      
      """
      Time complexity: O(nlogn), where n is the number of nodes in the given linked list. 
      This is because we are traversing the linked list to find the middle node and then recursively calling the constructBST function for the left and right halves of the list. 
      The time complexity of finding the middle node is O(n/2), which is equivalent to O(n) in the worst case. We do this O(logn) times, so the overall time complexity is O(nlogn).
Space complexity: O(logn), where n is the number of nodes in the given linked list. This is because we are creating a new TreeNode for each node in the BST. 
The maximum number of nodes in the BST is n, which occurs when the linked list is already sorted in ascending order. Since we are creating a balanced BST, the height of the tree is logn, so the space complexity is O(logn). 
The recursive calls also add to the space complexity, but since they are tail-recursive, the space used by them is optimized by the compiler and does not add to the overall space complexity.
"""
