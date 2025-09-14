import java.util.*;

class KthLargest {
    private PriorityQueue<Integer> pq;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.pq = new PriorityQueue<>(k);

        for(int num : nums){
            add(num);
        }
    }
    
    public int add(int val) {
        if(pq.size()<k){
            pq.offer(val);
        }else if(val>pq.peek()){
            pq.poll();
            pq.offer(val);
        }
        return pq.peek();
    }
}

// k = 3, nums = [4,5,8,2]
// Step by step:

// Heap empty → add 4 → [4]

// Add 5 → [4,5]

// Add 8 → [4,5,8] → heap now full (size = 3)

// Add 2 → 2 < 4 → ignore → [4,5,8]

// ✅ Heap after constructor = [4,5,8] (3 largest numbers)

// Top of heap = 4 → 3rd largest number

// Heap = [4,5,8]

// add(3) → 3 < 4 → ignore → heap = [4,5,8] → kth largest = 4

// add(5) → 5 > 4 → remove 4, add 5 → heap = [5,5,8] → kth largest = 5

// add(10) → 10 > 5 → remove 5, add 10 → heap = [5,10,8] → kth largest = 5

// add(9) → 9 > 5 → remove 5, add 9 → heap = [8,9,10] → kth largest = 8

// add(4) → 4 < 8 → ignore → heap = [8,9,10] → kth largest = 8

// Input:
// ["KthLargest", "add", "add", "add", "add", "add"]
// [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

// Output: [null, 4, 5, 5, 8, 8]