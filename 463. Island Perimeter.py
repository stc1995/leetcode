class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i_len = len(grid)
        j_len = len(grid[0]) if i_len else 0
        num_3, num_2, num_1 = 0, 0, 0
        visited = set()

        def dfs(i, j):
            for di, dj in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                ni, nj = i+di, j+dj
                if grid[ni][nj] == 1 and (ni, nj) not in visited:
                    if ((grid[ni+1][nj] == 1 and grid[ni][nj+1] == 1 and grid[ni-1][nj] == 1)
                        or (grid[ni][nj-1] == 1 and grid[ni][nj+1] == 1 and grid[ni-1][nj] == 1)
                        or (grid[ni-1][nj] == 1 and grid[ni+1][nj] == 1 and grid[ni][nj-1] == 1)
                        or (grid[ni+1][nj] == 1 and grid[ni][nj+1] == 1 and grid[ni][nj-1] == 1)):
                        num_3 = num_3 + 1
                    elif ((grid[ni+1][nj] == 1 and grid[ni][nj+1] == 1) or (grid[ni][nj+1] == 1 and grid[ni-1][nj] == 1)
                        or (grid[ni-1][nj] == 1 and grid[ni][nj-1] == 1) or (grid[ni+1][nj] == 1 and grid[ni][nj-1] == 1)
                        or (grid[ni-1][nj] == 1 and grid[ni+1][nj] == 1) or (grid[ni][nj-1] == 1 and grid[ni][nj+1] == 1)):
                        num_2 = num_2 + 1
                    elif grid[ni-1][nj] == 1 or grid[ni+1][nj] == 1 or grid[ni][nj-1] == 1 or grid[ni][nj + 1] == 1:
                        num_1 = num_1 + 1
                    visited.add((ni, nj))
                    dfs(ni, nj)

        for i in range(i_len):
            for j in range(j_len):
                if grid[i][j] == 1:
                    if grid[i][j] == 1 and (i, j) not in visited:
                        if ((grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i - 1][j] == 1)
                            or (grid[i][j - 1] == 1 and grid[i][j + 1] == 1 and grid[i - 1][j] == 1)
                            or (grid[i - 1][j] == 1 and grid[i + 1][j] == 1 and grid[i][j - 1] == 1)
                            or (grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i][j - 1] == 1)):
                            num_3 = num_3 + 1
                        elif ((grid[i + 1][j] == 1 and grid[i][j + 1] == 1) or (grid[i][j + 1] == 1 and grid[i - 1][j] == 1)
                              or (grid[i - 1][j] == 1 and grid[i][j - 1] == 1) or (grid[i + 1][j] == 1 and grid[i][j - 1] == 1)
                              or (grid[i - 1][j] == 1 and grid[i + 1][j] == 1) or (grid[i][j - 1] == 1 and grid[i][j + 1] == 1)):
                            num_2 = num_2 + 1
                        elif grid[i - 1][j] == 1 or grid[i + 1][j] == 1 or grid[i][j - 1] == 1 or grid[i][j + 1] == 1:
                            num_1 = num_1 + 1
                    visited.add((i, j))
                    dfs(i, j)
        return num_3*3+num_2*2+num_1


s = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(s.islandPerimeter(grid))

