import java.util.*;

 class InorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        inorder(root, result);

        return result;
    }

    public void inorder(TreeNode node, ArrayList<Integer> result){
        if(node == null) return;

        inorder(node.left, result);

        result.add(node.val); // this happens after the left subtree is fully visited.

        inorder(node.right, result);
    }
}
