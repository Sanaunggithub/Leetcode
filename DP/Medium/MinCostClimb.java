class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] mem = new int[cost.length];
        Arrays.fill(mem, -1);

        return Math.min(helper(0, cost, mem), helper(1, cost, mem));
    }

    public int helper(int n, int[] cost, int[] mem) {
        // base case: if past the last step, no cost
        if (n >= cost.length) return 0;

        // memoization check
        if (mem[n] != -1) return mem[n];

        // recursive case
        mem[n] = cost[n] + Math.min(helper(n + 1, cost, mem),
                                    helper(n + 2, cost, mem));
        return mem[n];
    }
}