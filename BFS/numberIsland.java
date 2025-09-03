import java.util.*;

class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int count = 0;

        Queue<int[]> queue = new LinkedList<>();
        int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Scan the entire grid
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                // Found a new island!
                if(grid[i][j] == '1' && !visited[i][j]){
                    count += 1;
                
                    queue.offer(new int[]{i, j});
                    visited[i][j] = true;
                    
                    while(!queue.isEmpty()){
                        int[] cell = queue.poll();
                        int r = cell[0], c = cell[1];
                        
                        // Check all 4 directions
                        for(int[] d : dirs){
                            int nr = r + d[0], nc = c + d[1];
                            
                            if(nr >= 0 && nr < rows && nc >= 0 && nc < cols && 
                               !visited[nr][nc] && grid[nr][nc] == '1'){
                                visited[nr][nc] = true;
                                queue.offer(new int[]{nr, nc});
                            }
                        }
                    }
                    // Island completely explored, continue scanning for next island
                }
            }
        }
        
        return count;
    }
}

// DFS
// class Solution {

//     public void dfs(char[][] grid, int i, int j){
//         if(i<0 || j<0 || i>=grid.length || j>=grid[0].length || grid[i][j]=='0') return;

//         grid[i][j] = '0';

//         dfs(grid, i+1, j);
//         dfs(grid, i-1, j);
//         dfs(grid, i, j+1);
//         dfs(grid, i, j-1);
//     }


//     public int numIslands(char[][] grid) {
//         int islands = 0;
//         for(int i=0; i<grid.length; i++){
//             for(int j=0; j<grid[0].length; j++){
//                 if(grid[i][j] == '1'){
//                     islands++;
//                     dfs(grid, i, j);
//                 }
//             }
//         }

//         return islands;
//     }
// }