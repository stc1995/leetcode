# 1、思考完一般情况后，要再想一下最边上的情况，以及和中间状态相对的初始状态
# 2、注意python与cpp、java不同，python数组下标为负后，并不报错，其逆向查询，但也会越界
# 3、=和==，在if中。平时编程时，默念“赋值”、“等于”，以区分
# 4、solution2中，算核心内容之前，先判断有没有越界等简单的异常，判异常之前先完成所有调整
# 5、没有括号提示，注意缩进，想想“这部分该在哪算？”

# solution 2 DFS
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        i_len = len(board)
        j_len = len(board[0])
        s = set([])
        count = 0

        def dfs(i, j):
            for di, dj in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                ni, nj = i+di, j+dj
                if 0 <= ni < i_len and 0 <= nj < j_len:
                    if board[ni][nj] == 'X' and (ni, nj) not in s:
                        s.add((ni, nj))
                        dfs(ni, nj)

        for i in range(i_len):
            for j in range(j_len):
                if board[i][j] == "X" and (i, j) not in s:
                    s.add((i, j))
                    dfs(i, j)
                    count += 1

        return count

# solution 1
# class Solution(object):
#     def countBattleships(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: int
#         """
#         i_len = len(board)
#         j_len = len(board[0])
#
#         count = 0
#         for i in range(i_len):
#             for j in range(j_len):
#                 if board[i][j] == 'X':
#                     if i > 0 and board[i-1][j] == "X":
#                         continue
#                     if j > 0 and board[i][j-1] == "X":
#                         continue
#                     count += 1
#         return count

board = ["X..X", "...X", "...X"]
s = Solution()
print(s.countBattleships(board))
