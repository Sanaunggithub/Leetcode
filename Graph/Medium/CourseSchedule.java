import java.util.*;

class Solution {
    Map<Integer, List<Integer>> graph;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        graph = new HashMap<>();

        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] p : prerequisites) {
            graph.get(p[0]).add(p[1]);
        }

        boolean[] visited = new boolean[numCourses];

        // graph may be disconnected
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, visited))
                return false;
        }
        return true;
    }

    public boolean dfs(int c, boolean[] visited) {
        if (visited[c])
            return false;

        if (graph.get(c).isEmpty())
            return true;

        visited[c] = true;

        for (int n : graph.get(c)) {
            if (!dfs(n, visited))
                return false;
        }

        // backtracking
        visited[c] = false;
        graph.get(c).clear();
        return true;
    }
}