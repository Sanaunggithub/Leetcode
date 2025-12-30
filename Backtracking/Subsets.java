import java.util.*;

class Subsets {
    List<Integer> curr = new ArrayList<>();
    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        dfs(0, nums);
        return result;
    }

    public void dfs(int i, int[] nums) {
        if (i == nums.length) {
            result.add(new ArrayList<>(curr));
            return;
        }

        // include
        curr.add(nums[i]);
        dfs(i + 1, nums);

        // not include
        curr.remove(curr.size() - 1);
        dfs(i + 1, nums);
    }

}