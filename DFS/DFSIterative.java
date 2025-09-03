import java.util.*;

public class DFSIterative {
    static void dfs(int start, List<List<Integer>> adj) {
        boolean[] visited = new boolean[adj.size()];
        Stack<Integer> stack = new Stack<>();
        stack.push(start);

        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (!visited[node]) {
                visited[node] = true;
                System.out.print(node + " ");
                
                // Push all unvisited neighbors to stack
                for (int neighbor : adj.get(node)) {
                    if (!visited[neighbor]) {
                        stack.push(neighbor);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        int n = 5;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        adj.get(0).add(1); adj.get(1).add(0);
        adj.get(0).add(2); adj.get(2).add(0);
        adj.get(1).add(3); adj.get(3).add(1);
        adj.get(1).add(4); adj.get(4).add(1);

        System.out.println("DFS starting from node 0:");
        dfs(0, adj);
    }
}


//    0
//   / \
//  1   2
// / \
// 3  4


// 0 → [1, 2]
// 1 → [0, 3, 4]
// 2 → [0]
// 3 → [1]
// 4 → [1]
