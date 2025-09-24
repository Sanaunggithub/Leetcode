import java.util.*;

class Solution {
    public int thirdMax(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();     
        Set<Integer> seen = new HashSet<>();

        for(int n:nums){
            if(seen.add(n)){
                pq.offer(n);
            }

            if(pq.size() > 3){
                pq.poll(); // keep only top 3
            }
        }

        if(pq.size() == 3){
            return pq.peek();
        }
        else{
            return Collections.max(pq); //  find the largest element in the heap
        }
        
    }
}


// nums = [10, 9, 8, 7]

// Start: pq = []

// Add 10 → pq = [10]

// Add 9 → pq = [9,10]

// Add 8 → pq = [8,10,9]

// Add 7 → pq = [7,8,9,10] → size = 4, so we poll() smallest → pq = [8,10,9]