from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        mp = {}
        for i, val in enumerate(inorder):
            mp[val] = i
        
        def helper(l, r, p_idx):
            if l < 0 or l >= N or r < 0 or r >= N or p_idx >= N:
                return None
            pre_val = preorder[p_idx]
            inorder
            i_idx = mp[pre_val]
            node = TreeNode(pre_val)
            node.left = helper(l, i_idx - 1, p_idx + 1)
            node.right = helper(i_idx + 1, r, p_idx + 1)
            return node
        return helper(0, N - 1, 0)

Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])