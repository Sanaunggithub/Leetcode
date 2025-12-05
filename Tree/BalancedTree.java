class Solution {
    public boolean isBalanced(TreeNode root) {
        return dfs(root) != -1; // True when root is not -1
    }

    private int dfs(TreeNode root) {
        if (root == null)
            return 0;

        int left = dfs(root.left);
        if (left == -1)
            return -1; // left subtree unbalanced

        int right = dfs(root.right);
        if (right == -1)
            return -1; // right subtree unbalanced

        if (Math.abs(left - right) > 1)
            return -1; // unbalanced

        return 1 + Math.max(left, right);
    }
}
