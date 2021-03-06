from collections import deque

from LeetCode.DS import TreeNode


class Solution:
    def maxDepth_old(self, root: TreeNode) -> int:
        if not root: return 0
        depth = 0

        que = deque([root])
        while que:
            n = len(que)
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            depth += 1

        return depth

    def maxDepth(self, root: TreeNode) -> int:
        """
        Idea: BFS, as long as it ends, return the level
        """
        from collections import deque
        que = deque()
        que.append((root, 1))
        level = 0
        if not root:
            return 0
        while que:
            node, level = que.pop()
            if node.left:
                que.appendleft((node.left, level + 1))
            if node.right:
                que.appendleft((node.right, level + 1))
        return level
