class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hor=[]
        ver=[]
        squ=[]
        for i in range(9):
            hor.append([n for n in board[i] if n!="."])
            ver.append([n[i] for n in board if n[i]!="."])
        for i in range(3):
            for j in range(3):
                l=[]
                for a in range(3):
                    for b in range(3):
                        if (board[a+i*3][b+j*3])!=".":
                            l.append(board[a+i*3][b+j*3])
                squ.append(l)

        for i in hor:
            if not self.check(i): return False
        for i in ver:
            if not self.check(i): return False
        for i in squ:
            if not self.check(i): return False

        return True


    def check(self,l:list[int])->bool:
        return len(l)==len(set(l))


s=Solution()
print(s.isValidSudoku([
     [".",".",".",".","5",".",".","1","."]
    ,[".","4",".","3",".",".",".",".","."]
    ,[".",".",".",".",".","3",".",".","1"]
    ,["8",".",".",".",".",".",".","2","."]
    ,[".",".","2",".","7",".",".",".","."]
    ,[".","1","5",".",".",".",".",".","."]
    ,[".",".",".",".",".","2",".",".","."]
    ,[".","2",".","9",".",".",".",".","."]
    ,[".",".","4",".",".",".",".",".","."]]))
