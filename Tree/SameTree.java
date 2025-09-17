class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
        if(p == null && q == null) {
            return true;
        }

        else if(p == null || q == null){
            return false;
        }

        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}

/*
p:       1             q:        1
        / \                     / \
       2   3                   2   3

Example trace for trees above:

isSameTree(1,1)
    -> p.val == q.val? 1==1 → true
    -> isSameTree(p.left=2, q.left=2)
        -> p.val == q.val? 2==2 → true
        -> isSameTree(p.left.left=null, q.left.left=null) → true
        -> isSameTree(p.left.right=null, q.left.right=null) → true
        -> left & right true → return true
    -> isSameTree(p.right=3, q.right=3)
        -> p.val == q.val? 3==3 → true
        -> isSameTree(p.right.left=null, q.right.left=null) → true
        -> isSameTree(p.right.right=null, q.right.right=null) → true
        -> left & right true → return true
    -> root: 1==1 && left true && right true → return true
*/