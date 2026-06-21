# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = {}

        def inorder(root , idx):
            if not root:
                return 
            inorder(root.left , idx + 1)
            if idx not in level:
                level[idx] = []
            level[idx].append(root.val)
            inorder(root.right , idx + 1)
        
        inorder(root , 0)
        res = []

        for k in sorted(level.keys()):
            res.append(level[k])
        return res
        