import java.util.*;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {

        Map<Integer, List<int[]>> graph = new HashMap();

        for(int[] t: times){
            int u = t[0] - 1; //source node (0-based)
            int v = t[1] - 1;
            int w = t[2];

            if (!graph.containsKey(u)) {
                graph.put(u, new ArrayList<>());
            }
            graph.get(u).add(new int[]{v, w});
        }

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[k - 1] = 0; // 0-based

        // minimum distance will be top
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, k - 1}); // {distance, node}

        while(!pq.isEmpty()){
            int[] curr = pq.poll();
            int dist = curr[0];
            int u = curr[1];

            if (dist > distance[u]) continue;

            for(int[] edge : graph.getOrDefault(u, new ArrayList<>())){
                int v = edge[0];
                int w = edge[1];

                if(distance[u] != Integer.MAX_VALUE && distance[u] + w < distance[v]){
                    distance[v] = distance[u] + w;
                    pq.offer(new int[] {distance[v], v});
                }
            }
        }

        int ans = 0;
        for (int d : distance) {
            if (d == Integer.MAX_VALUE) return -1;  // unreachable node
            ans = Math.max(ans, d);
        }
        return ans;
    }
}