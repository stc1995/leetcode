# 1、思考完一般情况后，要再想一下最边上的情况，以及和中间状态相对的初始状态
# 2、注意python与cpp、java不同，python数组下标为负后，并不报错，其逆向查询，但也会越界

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        i_len = len(board)
        j_len = len(board[0])
        
        count = 0
        for i in range(i_len):
            for j in range(j_len):
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == "X":
                        continue
                    if j > 0 and board[i][j-1] == "X":
                        continue
                    count += 1
        return count

board = ["X..X", "...X", "...X"]
print(board[-1][0])
print(board[0][-1])
s = Solution()
print(s.countBattleships(board))