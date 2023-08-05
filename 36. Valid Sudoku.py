class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            dic = {}
            for j in row:
                if j != ".":
                    if dic.get(j,0):
                        return False
                    else:
                        dic [j] = 1

        for i in range(len(board)) :
            dic = {}
            for j in range (len(board[i])):
                if board[j][i] !=".":
                    if dic.get(board[j][i],0):
                        return False
                    else:
                        dic [board[j][i]] = 1
        for z in range(3):
            for i in range (3):
                dic ={}
                for j in range(3):
                
                    for k in range(3):
                        if board[3*z+j][3*i+k] !=".":
                            if dic.get(board[3*z+j][3*i+k],0):
                                return False
                            else:
                                dic [board[3*z+j][3*i+k]] = 1
        return True
