# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)
        
#         if val > root.val:
#             root.right = self.insertIntoBST(root.right, val)
#         else:
#             root.left = self.insertIntoBST(root.left,val)
#         return root

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # try with iteration
        if not root:
            return TreeNode(val)

        curr = root
        while True:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return root
            elif val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return root
        return root

        
