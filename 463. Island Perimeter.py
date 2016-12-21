#  1、在穷举情况时，想想能否反过来，或者用其他方法来提炼穷举的共同点，简化问题
#  2、用减法来规避处理矩阵边上的边
#  3、在类内部的函数，参数不要忘写self，否则无论是类定义的对象的调用还是类内部的self调用，都会显示参数多给了
#     函数中只供自己使用的可以不写self
#  4、全局、局部变量，不修改则不用写global，一切顺利；要修改，见：http://f.dataguru.cn/thread-133513-1-1.html
    # def fun1():
    #     global i
    #     i = 0
    #     def fun2():
    #         global i
    #         y = i + 1
    #         i = y
    #         return i
    #     return fun2
    # a = fun1()
    # print a()

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i_len = len(grid)
        j_len = len(grid[0])
        count = 0
        if i_len == 0 and j_len == 0:
            return 0
        for i in range(i_len):
            for j in range(j_len):
                if grid[i][j]:
                    count += 4*grid[i][j]
                    if i > 0 and grid[i-1][j] == 1:
                        count -= 1
                    if j > 0 and grid[i][j-1] == 1:
                        count -= 1
                    if j < j_len-1 and grid[i][j + 1] == 1:
                        count -= 1
                    if i < i_len-1 and grid[i+1][j] == 1:
                        count -= 1
        return count


        #  method 2
        # i_len = len(grid)
        # j_len = len(grid[0])
        #
        # def countEdge(i, j):
        #     a = [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]
        #     count = 4
        #     for i in a:
        #         if -1 < i[0] < i_len and -1 < i[1] < j_len:
        #             if grid[i[0]][i[1]]:
        #                 count -= 1
        #     return count
        #
        # return sum(countEdge(i, j) for i in range(i_len) for j in range(j_len) if grid[i][j]) ##########################################
        ##################################################################################################################################

    #     method 1
    # def islandPerimeter(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     global i_len, j_len
    #     i_len = len(grid)
    #     j_len = len(grid[0])
    #     ans = 0
    #
    #     for i in range(i_len):
    #         for j in range(j_len):
    #             if grid[i][j] == 1:
    #                 ans = ans + self.countEdge(i, j)
    #     return ans
    #
    # def countEdge(self, i, j):  # 提交时，显示grid不是全局变量，因此改为def countEdge(self, i, j， grid):  上面也相应改为ans = ans + self.countEdge(i, j， grid)
    #
    #     a = [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]
    #     count = 4
    #     global i_len, j_len
    #     for i in a:
    #         if -1 < i[0] < i_len and -1 < i[1] < j_len:
    #             if grid[i[0]][i[1]]:
    #                 count -= 1
    #     return count


        #   太复杂
        # i_len = len(grid)
        # j_len = len(grid[0]) if i_len else 0
        # global num_3, num_2, num_1
        # num_3, num_2, num_1 = 0, 0, 0
        # visited = set()
        #
        # def dfs(i, j):
        #     global num_1
        #     global num_2
        #     global num_3
        #     for di, dj in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        #         ni, nj = i+di, j+dj
        #         if grid[ni][nj] == 1 and (ni, nj) not in visited:
        #             if (grid[ni+1][nj] == 1 and grid[ni][nj+1] == 1 and grid[ni-1][nj] == 1) or (grid[ni][nj-1] == 1 and grid[ni][nj+1] == 1 and grid[ni-1][nj] == 1) or (grid[ni-1][nj] == 1 and grid[ni+1][nj] == 1 and grid[ni][nj-1] == 1) or (grid[ni+1][nj] == 1 and grid[ni][nj+1] == 1 and grid[ni][nj-1] == 1):
        #                 num_1 = num_1 + 1
        #             elif (grid[ni+1][nj] == 1 and grid[ni][nj+1] == 1) or (grid[ni][nj+1] == 1 and grid[ni-1][nj] == 1) or (grid[ni-1][nj] == 1 and grid[ni][nj-1] == 1) or (grid[ni+1][nj] == 1 and grid[ni][nj-1] == 1) or (grid[ni-1][nj] == 1 and grid[ni+1][nj] == 1) or (grid[ni][nj-1] == 1 and grid[ni][nj+1] == 1):
        #                 num_2 = num_2 + 1
        #             elif grid[ni-1][nj] == 1 or grid[ni+1][nj] == 1 or grid[ni][nj-1] == 1 or grid[ni][nj + 1] == 1:
        #                 num_3 = num_3 + 1
        #             visited.add((ni, nj))
        #             dfs(ni, nj)
        #
        # for i in range(i_len):
        #     for j in range(j_len):
        #         if grid[i][j] == 1:
        #             if grid[i][j] == 1 and (i, j) not in visited:
        #                 if ((grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i - 1][j] == 1)
        #                     or (grid[i][j - 1] == 1 and grid[i][j + 1] == 1 and grid[i - 1][j] == 1)
        #                     or (grid[i - 1][j] == 1 and grid[i + 1][j] == 1 and grid[i][j - 1] == 1)
        #                     or (grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i][j - 1] == 1)):
        #                     num_3 = num_3 + 1
        #                 elif ((grid[i + 1][j] == 1 and grid[i][j + 1] == 1) or (grid[i][j + 1] == 1 and grid[i - 1][j] == 1)
        #                       or (grid[i - 1][j] == 1 and grid[i][j - 1] == 1) or (grid[i + 1][j] == 1 and grid[i][j - 1] == 1)
        #                       or (grid[i - 1][j] == 1 and grid[i + 1][j] == 1) or (grid[i][j - 1] == 1 and grid[i][j + 1] == 1)):
        #                     num_2 = num_2 + 1
        #                 elif grid[i - 1][j] == 1 or grid[i + 1][j] == 1 or grid[i][j - 1] == 1 or grid[i][j + 1] == 1:
        #                     num_1 = num_1 + 1
        #             visited.add((i, j))
        #             dfs(i, j)
        # return num_3*3+num_2*2+num_1


s = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(s.islandPerimeter(grid))

