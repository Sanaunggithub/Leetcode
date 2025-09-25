class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;
    
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));

    }    

}   

// Step 1: Call on root (3)

// maxDepth(3) → not null →
// 1 + Math.max(maxDepth(9), maxDepth(20))

// Step 2: Left side (9)

// maxDepth(9) → not null →
// 1 + Math.max(maxDepth(null), maxDepth(null))

// Both children are null, so:
// maxDepth(null) = 0

// So:
// maxDepth(9) = 1 + Math.max(0, 0) = 1

// Step 3: Right side (20)

// maxDepth(20) → not null →
// 1 + Math.max(maxDepth(15), maxDepth(7))

// maxDepth(15) → leaf → 1

// maxDepth(7) → leaf → 1

// So:
// maxDepth(20) = 1 + Math.max(1, 1) = 2

// Step 4: Back to root (3)

// Now substitute values:
// maxDepth(3) = 1 + Math.max(1, 2)
// = 1 + 2
// = 3

// ✅ Final Output: 3

// Which matches the longest path:
// 3 → 20 → 15 (or 3 → 20 → 7) has 3 nodes.
