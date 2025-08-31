import java.util.*;

class Solution {
    public int islandPerimeter(int[][] grid) {

        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[rows][cols];

        int count = 0;
        boolean found = false;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(grid[i][j] == 1){
                    queue.offer(new int[]{i, j});
                    visited[i][j] = true;
                    found = true;
                    break; // only exit inner loop
                }
            }

            if(found) break; // that's why second break is needed
        }

        int [][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while(!queue.isEmpty()){
            int [] cell = queue.poll();
            int r = cell[0], c = cell[1];


            for(int[] d : dirs){
                int nr = r + d[0], nc = c + d[1];

                // if it is water or out of bound. Parameter is next to water or at the boundary of the grid(no neighbour)
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == 0) {
                        count += 1;
                } else if (!visited[nr][nc]) {
                    queue.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            
            } 
        }

        return count;
    }
}