class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;

        for(int n : nums){
            sum += n;
        }

        if(sum % 2 != 0) return false;
        
        int target = sum / 2;
        Boolean [][] memo = new Boolean[nums.length][target + 1];

        return helperMemo(nums, 0, target, memo);
    }

    private  boolean helperMemo(int[] arr, int index, int target, Boolean[][] memo) {
        if (target == 0) return true;
        if (index == arr.length || target < 0) return false;

        if (memo[index][target] != null) return memo[index][target];

        boolean res = helperMemo(arr, index + 1, target - arr[index], memo) ||
                      helperMemo(arr, index + 1, target, memo);

        return memo[index][target] = res;
    }

}