import java.util.*;

class findKthLargestSolution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int n: nums){
            pq.offer(n);
            if(pq.size() > k){
                pq.poll();
            }
        }

        return pq.peek();
    }
}