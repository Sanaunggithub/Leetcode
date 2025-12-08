class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length];
        backtrack(nums, used, 0, new ArrayList<Integer>(),result);

        return result;
    }
    public void backtrack(int[] nums, boolean[] used , int level, List<Integer> tmp,
    List<List<Integer>> result){
        if (level == nums.length){
            result.add(new ArrayList<Integer>(tmp));
        }

        for(int i = 0; i < nums.length; i++){
            if(used[i] == false){
                used[i] = true;
                tmp.add(nums[i]);
                backtrack(nums, used, level + 1, tmp, result);
                used[i] = false;
                tmp.remove(tmp.size() - 1);
            }
        }
    }
}