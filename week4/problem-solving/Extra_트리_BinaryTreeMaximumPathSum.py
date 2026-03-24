# 트리 - Binary Tree Maximum Path Sum
# 문제 링크: https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        #후위 순회:
        def post_order(node):
            if not node:
                return 0
            
            left_gain = max(post_order(node.left), 0)
            right_gain = max(post_order(node.right), 0)

            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(current_path_sum, self.max_sum)
            
            return max(left_gain, right_gain) + node.val
        post_order(root)
        return self.max_sum