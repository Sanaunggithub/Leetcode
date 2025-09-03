import java.util.*;

 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;         
    this.left = left;
    this.right = right;
    }
}
 
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

// 1
//  \
//   2
//  /
// 3

// [1, 3, 2]

// Step 1: Start at root (1)    
// Go to left: inorder(1.left) → inorder(null) → returns immediately.
// Now execute result.add(1) → result = [1]
// Move to right: inorder(2)

// Step 2: Node 2
// Go left: inorder(3)

// Step 3: Node 3
// Left = null → return
// Execute result.add(3) → result = [1, 3]
// Right = null → return
// Pop back to 2


// Step 4: Node 2 (back from left)
// Execute result.add(2) → result = [1, 3, 2]
// Right = null → returns
// Pop back to 1 → all done
