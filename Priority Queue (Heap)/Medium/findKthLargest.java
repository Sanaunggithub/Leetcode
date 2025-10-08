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

// nums = [3,2,1,5,6,4], k = 2

// Heap = [] → add 3 → [3]

// Add 2 → [2,3] (heap size ≤ k → keep both)

// Add 1 → [1,3,2] → size = 3 > k → remove 1 → [2,3]

// Add 5 → [2,3,5] → size = 3 → remove 2 → [3,5]

// Add 6 → [3,5,6] → size = 3 → remove 3 → [5,6]

// Add 4 → [4,6,5] → size = 3 → remove 4 → [5,6]

// ✅ Heap contains [5,6], the 2 largest numbers.

// Top of min-heap = 5 → 2nd largest element.