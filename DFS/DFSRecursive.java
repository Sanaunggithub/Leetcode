import java.util.*;

public class DFSRecursive {
    static void dfs(int node, boolean[] visited, List<List<Integer>> adj) {
        // Mark the current node as visited
        visited[node] = true;
        System.out.print(node + " ");

        // Recur for all adjacent nodes
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, visited, adj);
            }
        }
    }

    public static void main(String[] args) {
        int n = 5; // number of nodes
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Add edges (undirected graph)
        adj.get(0).add(1);
        adj.get(1).add(0);
        adj.get(0).add(2);
        adj.get(2).add(0);
        adj.get(1).add(3);
        adj.get(3).add(1);
        adj.get(1).add(4);
        adj.get(4).add(1);

        boolean[] visited = new boolean[n];
        System.out.println("DFS starting from node 0:");
        dfs(0, visited, adj);
    }
}

//    0
//   / \
//  1   2
// / \
// 3  4

// adj.get(node)
// 0 → [1, 2]
// 1 → [0, 3, 4]
// 2 → [0]
// 3 → [1]
// 4 → [1]

// Start at dfs(0, visited, adj)
// → visit 0, mark visited.

// From 0, go to neighbor 1
// → visit 1.

// From 1, go to neighbor 3
// → visit 3.

// From 3, only neighbor is 1 (already visited) → backtrack.

// Back to 1, next neighbor = 4
// → visit 4.

// From 4, only neighbor is 1 (already visited) → backtrack.

// Back to 1, all neighbors done → backtrack to 0.

// From 0, next neighbor = 2
// → visit 2.

// From 2, only neighbor is 0 (already visited) → backtrack.