import java.util.*;

class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        
        Queue<Integer> queue = new LinkedList<>();

        // First add students to queue
        for(Integer s: students){
            queue.offer(s);
        }

        int i = 0; int rotation = 0;

        while(!queue.isEmpty() && i < sandwiches.length){
            if(queue.peek() == sandwiches[i]){
                queue.poll();
                i++;
                rotation = 0;
            }

            else{
                queue.offer(queue.poll());
                rotation++;
            }
            
            // If every student rotated once but no sandwich taken -> stop
            if (rotation == queue.size()) {
                break;
            }
        }

        return queue.size();
    }   
}