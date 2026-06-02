class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size();          // number of rows
        int col = grid[0].size();       // number of columns
        int islandCount = 0;            // counts number of connected components (islands)

        // Traverse each cell in the grid
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {

                // Skip if the current cell is water ('0')
                if (grid[i][j] == '0') continue;

                // We found a land cell ('1') → New island detected
                islandCount++;

                // Use BFS to explore the entire island and mark it visited
                queue<pair<int, int>> qu;
                qu.push({i, j});
                grid[i][j] = '0';   // mark current cell as visited by turning it into water

                // BFS to visit all neighboring land cells
                while (!qu.empty()) {
                    auto current = qu.front();
                    qu.pop();
                    int r = current.first;
                    int c = current.second;

                    // Move UP
                    if (r - 1 >= 0 && grid[r - 1][c] == '1') {
                        qu.push({r - 1, c});
                        grid[r - 1][c] = '0';  // mark visited
                    }

                    // Move DOWN
                    if (r + 1 < row && grid[r + 1][c] == '1') {
                        qu.push({r + 1, c});
                        grid[r + 1][c] = '0';  // mark visited
                    }

                    // Move RIGHT
                    if (c + 1 < col && grid[r][c + 1] == '1') {
                        qu.push({r, c + 1});
                        grid[r][c + 1] = '0';  // mark visited
                    }

                    // Move LEFT
                    if (c - 1 >= 0 && grid[r][c - 1] == '1') {
                        qu.push({r, c - 1});
                        grid[r][c - 1] = '0';  // mark visited
                    }
                }
            }
        }
        return islandCount;  // return total number of islands found
    }
};
