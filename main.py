# Se o sudoku está valido com 9x9
# Cada linha deve ter o número de 1 a 9 sem repetição
# Cada coluna deve ter o número de 1 a 9 sem repetição
# Cada subcaixa 3x3 deve ter o número de 1 a 9 sem repetição 

class Solution(object):
  def isValidSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    self.board = board
    # Verificando 9x9
    scala = all(len(self.board[i]) == 9 for i in range(len(self.board[0])))
    # Verificando se são valores diferentes cada linha
    line = all(len(set(self.board[i])) - (9 - self.board[i].count('.')) == 1 for i in range(len(self.board[0])))
    # Verificando se são valores diferentes cada coluna -> Transform Transposta
    boardT = [[self.board[j][i] for j in range(len(self.board))] for i in range(len(self.board[0]))]
    # Retornando Booleano
    column = all(len(set(boardT[i])) - (9 - boardT[i].count('.')) == 1 for i in range(len(boardT[0])))
    # Quebrando 3x3
    for i in range(0, 9, 3):
      for c in range(0, 9, 3):
        boardSub = [self.board[x][y] for x in range(i, i + 3) for y in range(c, c + 3)]
        elements = [num for num in boardSub if num != '.']
        if len(elements) != len(set(elements)) or not all('1' <= num <= '9' for num in elements): return False
    
    # Se algum dos elementos for falso:
    if not scala or not line or not column: return False
    else: return True 
    
sudoku = Solution()


board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."], 
        [".","9","8",".",".",".",".","6","."], 
        ["8",".",".",".","6",".",".",".","3"], 
        ["4",".",".","8",".","3",".",".","1"], 
        ["7",".",".",".","2",".",".",".","6"], 
        [".","6",".",".",".",".","2","8","."], 
        [".",".",".","4","1","9",".",".","5"], 
        [".",".",".",".","8",".",".","7","9"]]

sudoku.isValidSudoku(board) # Output True