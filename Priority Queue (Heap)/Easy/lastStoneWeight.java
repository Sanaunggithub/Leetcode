class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int lastStoneWeight = 0;
        for(int s : stones){
            pq.add(s);
        }

        while(pq.size() > 1){
            int stone1 = pq.poll();
            int stone2 = pq.poll();

            if(stone1 != stone2){
                pq.add(stone1 - stone2);
            }
        }

        lastStoneWeight = pq.isEmpty() ? 0 : pq.poll();
        return lastStoneWeight;
    }
}