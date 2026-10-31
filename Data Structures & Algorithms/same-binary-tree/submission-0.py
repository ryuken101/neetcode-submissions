# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # initialise stack with tuple containing the root nodes for both trees
        stack = [(p,q)]
        # Continues processing as long as there are pairs of nodes left to compare.
        while stack: 
            # Pops the most recent pair of nodes from the stack.
            node1, node2 = stack.pop()
            #If both nodes are None, it means this branch matches structurally at its end, so it safely skips to the next iteration.
            if not node1 and not node2: 
                continue 
            #Checks for structural or value mismatches. It returns False immediately if:
	# One node exists while the other is None (structural mismatch).
	# Both exist but their values do not match (value mismatch).
            if not node1 or not node2 or node1.val != node2.val: 
                return False
            # Pushes the right children and then the left children onto the stack. Because a stack is Last-In, First-Out (LIFO), pushing the left child last ensures it is processed first, maintaining a traditional pre-order traversal sequence
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True 
            



        