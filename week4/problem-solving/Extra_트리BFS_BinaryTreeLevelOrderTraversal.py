# 트리, BFS - Binary Tree Level Order Traversal
# 문제 링크: https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        #일단 bfs 순회
        def bfs():
            # q 생성 및 초기화
            q = deque([(root, 1)]) #[0]은 노드 [1]은 레벨
            result = {}
            while q:
                node, level = q.popleft()
                if level not in result:
                    result[level] = [node.val]
                else:
                    result[level].append(node.val)

                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            return result
        res_dict = bfs()
        return [res_dict[i] for i in sorted(res_dict.keys())]
