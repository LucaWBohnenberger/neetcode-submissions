class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Linhas
        for linha in range(9):   
            valores = dict()
            for coluna in range(9):
                if board[linha][coluna] != ".":
                    val = valores.get(board[linha][coluna], 0)
                    if val == 0:
                        valores[board[linha][coluna]] = 1
                    else:
                        return False 
        
        #Coluna
        for coluna in range(9):   
            valores = dict()
            for linha in range(9):
                if board[linha][coluna] != ".":
                    val = valores.get(board[linha][coluna], 0)
                    if val == 0:
                        valores[board[linha][coluna]] = 1
                    else:
                        return False 

        # Bloco
        for bloco_coluna in [0,3,6]:
            for bloco_linha in [0,3,6]:
                valores = dict()
                for linha in range(0,3):
                    for coluna in range(0,3):
                        if board[linha+bloco_linha][coluna+bloco_coluna] != ".":
                            val = valores.get(board[linha+bloco_linha][coluna+bloco_coluna], 0)
                            if val == 0:
                                valores[board[linha+bloco_linha][coluna+bloco_coluna]] = 1
                            else:
                                return False 

        return True