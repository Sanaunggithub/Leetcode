import java.util.ArrayList;
import java.util.List;

import javax.swing.tree.TreeNode;

public class PreOrder {
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        preorder(root, result);
        return result;
    }

    public void preorder(TreeNode root, ArrayList<Integer> result){

        if(root == null) return;
        result.add(root.val);
        preorder(root.left, result);    
        preorder(root.right, result);
    }
}
/* 

             1
          /     \
        2         3
      /   \        \
     4     5        8
         /   \
        6     7
             /
            9

*/

// Start: preorder(1)

// result = [1]

// Call preorder(2)

// preorder(2)

// result = [1, 2]

// Call preorder(4)

// preorder(4)

// result = [1, 2, 4]

// Left is null → return

// Right is null → return

// Back to 2

// Back at 2 → now preorder(5)

// result = [1, 2, 4, 5]

// Call preorder(6)

// preorder(6)

// result = [1, 2, 4, 5, 6]

// Left null → return

// Right null → return

// Back to 5

// Back at 5 → now preorder(7)

// result = [1, 2, 4, 5, 6, 7]

// Call preorder(9)

// preorder(9)

// result = [1, 2, 4, 5, 6, 7, 9]

// Left null → return

// Right null → return

// Back to 7 → done

// Back to 5 → done

// Back to 2 → done

// Back to 1

// Back at 1 → now preorder(3)

// result = [1, 2, 4, 5, 6, 7, 9, 3]

// Left is null → skip

// Call preorder(8)

// preorder(8)

// result = [1, 2, 4, 5, 6, 7, 9, 3, 8]

// Left null → return

// Right null → return

// ✅ Final result = [1, 2, 4, 5, 6, 7, 9, 3, 8]