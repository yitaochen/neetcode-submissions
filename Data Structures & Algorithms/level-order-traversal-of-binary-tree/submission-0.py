# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # obvious BFS 
        if not root:
            return []
        dq = deque([root])
        ans = []
        while dq:
            level_ans = []
            for i in range(len(dq)):
                cur = dq.popleft()
                level_ans.append(cur.val)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            ans.append(level_ans)
        
        return ans 
