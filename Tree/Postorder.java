/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        postOrder(root, result);

        return result;
    }

    public void postOrder(TreeNode root, ArrayList<Integer> result){
        if(root == null) return;
        postOrder(root.left, result);
        postOrder(root.right, result);
        result.add(root.val);
    }
}

// Start: postorder(1)

// Go left → postorder(2)

// postorder(2)

// Go left → postorder(4)

// postorder(4)

// Left null → return

// Right null → return

// Visit 4 → result = [4]

// Back to 2 → go right → postorder(5)

// postorder(5)

// Go left → postorder(6)

// postorder(6)

// Left null → return

// Right null → return

// Visit 6 → result = [4, 6]

// Back to 5 → go right → postorder(7)

// postorder(7)

// Left null → return

// Right → postorder(9)

// postorder(9)

// Left null → return

// Right null → return

// Visit 9 → result = [4, 6, 9]

// Back to 7 → visit 7 → result = [4, 6, 9, 7]

// Back to 5 → visit 5 → result = [4, 6, 9, 7, 5]

// Back to 2 → visit 2 → result = [4, 6, 9, 7, 5, 2]

// Back at 1 → go right → postorder(3)
// postorder(3)

// Left null → skip

// Right → postorder(8)

// postorder(8)

// Left null → skip

// Right null → skip

// Visit 8 → result = [4, 6, 9, 7, 5, 2, 8]

// Back to 3 → visit 3 → result = [4, 6, 9, 7, 5, 2, 8, 3]

// Back at 1 → visit 1 → result = [4, 6, 9, 7, 5, 2, 8, 3, 1]