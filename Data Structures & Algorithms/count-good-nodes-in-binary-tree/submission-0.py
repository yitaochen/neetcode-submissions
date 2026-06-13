# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS / BFS needs to pass max info
        ans = [0]
        def dfs(node, MAX):
            if not node:
                return 
            if node.val >= MAX:
                ans[0] += 1
            dfs(node.left, max(MAX, node.val))
            dfs(node.right, max(MAX, node.val))
        
        dfs(root, root.val)

        return ans[0]