def binaryTreePaths(self, root):
        # tree with one node
        if not root:
            return []

        result = []

        def dfs(root, tmp):
            if not root: return

            tmp.append(str(root.val))

            if not root.left and not root.right:
                result.append("->".join(tmp))

            else: 
                dfs(root.left, tmp)
                dfs(root.right, tmp)
            tmp.pop()

        dfs(root, [])
        return result