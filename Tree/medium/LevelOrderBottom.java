class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        levelOrderBottom(root, result);
        Collections.reverse(result);
        return result;
    }

    public void levelOrderBottom(TreeNode root, List<List<Integer>> result){
        if(root == null) return;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){
            int size = queue.size();
            
            List<Integer> lst = new ArrayList<>();
            for(int i = 0; i < size; i++){
                TreeNode curr = queue.poll();
                lst.add(curr.val);

                if(curr.left!=null) queue.offer(curr.left);
                if(curr.right != null) queue.offer(curr.right);
            }
            result.add(lst);
        }

    }
}