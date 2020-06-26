"""
this class is responsible for all of the chess games logic and storing data
"""

class GameState():
    def __init__(self):
        self.board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                      ["bP","bP","bP","bP","bP","bP","bP","bP"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["wP","wP","wP","wP","wP","wP","wP","wP"],
                      ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whiteToMove = True # white player always starts
        self.moveLog = []

    '''
    Takes a Move as a parameter and execute it, this will not work for castling, pawn promotion and en passant .. need to implement that later
    '''
    def makeMove(self, move):
        if self.board[move.start_row][move.start_col] != "--":
            self.board[move.start_row][move.start_col] = "--"
            self.board[move.end_row][move.end_col] = move.piece_moved
            self.moveLog.append(move) #log the move so we can undo later
            self.whiteToMove = not self.whiteToMove # to swap players

    '''
    Undo the last move made
    '''
    def undoMove(self):
        if len(self.moveLog) != 0: #make sure that there is a move to undo
            move = self.moveLog.pop()
            self.board[move.start_row][ move.start_col] = move.piece_moved
            self.board[move.end_row][ move.end_col] = move.piece_captured
            self.whiteToMove = not self.whiteToMove #switch turns back


    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves() # for now we will not worry about checks

    '''
    All possible moves
    '''
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): # number of cols in a given row
                turn = self.board[r][c][0] # the first char of a board piece represents the color 'w' or 'b'
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'P':
                        self.getPawnMoves(r,c,moves)
                    elif piece == 'R':
                        self.getRookMoves(r,c,moves)
                    elif piece == 'B':
                        self.getBishopMoves(r,c,moves)
                    elif piece == 'N':
                        self.getKnightMoves(r,c,moves)
                    elif piece == 'Q':
                        self.getQueenMoves(r,c,moves)
                    elif piece == 'K':
                        self.getKingMoves(r,c,moves)

        return moves


    '''
    Get all pawn moves for the pawn located at r, c and add these moves to the list
    '''
    def getPawnMoves(self, r, c, moves):
        pass

    '''
    Get all rook moves for the pawn located at r, c and add these moves to the list
    '''
    def getRookMoves(self, r, c, moves):
        pass

    '''
    Get all bishop moves for the pawn located at r, c and add these moves to the list
    '''
    def getBishopMoves(self, r, c, moves):
        pass

    '''
    Get all knight moves for the pawn located at r, c and add these moves to the list
    '''
    def getKnightMoves(self, r, c, moves):
        pass

    '''
    Get all queen moves for the pawn located at r, c and add these moves to the list
    '''
    def getQueenMoves(self, r, c, moves):
        pass

    '''
    Get all king moves for the pawn located at r, c and add these moves to the list
    '''
    def getKingMoves(self, r, c, moves):
        pass


class Move():

    # varriables to convert between chess notations and regular array notations
    ranks_to_rows = {"1":7,"2":6,"3":5,"4":4,
                     "5":3,"6":2,"7":1,"8":0}

    rows_to_ranks = {v: k for k,v in ranks_to_rows.items()}

    files_to_cols = {"a":0,"b":1,"c":2,"d":3,
                    "e":4,"f":5,"g":6,"h":7}

    cols_to_files = {v: k for k,v in files_to_cols.items()}

    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][ self.end_col]

    def getChessNotation(self):
        # can later be improved to work like real chess notation
        return self.getRankFile(self.start_row,self.start_col) + self.getRankFile(self.end_row, self.end_col)

    def getRankFile(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]