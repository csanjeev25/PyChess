from chess_utils import *

class Chess_Model(dict):
    captured_pieces = { 'white': [], 'black': [] }
    player_turn = None
    no_of_turns_since_last_capture_or_pawn_move = 0 #for chess 50 move rule
    moves = 1
    history = []

    def __init__(self):

    def get_piece_at(self,position):
        return self.get(position)

    def get_alphanumeric_position(self, rowcol):
        if self.is_on_board(rowcol):
            row, col = rowcol
            return "{}{}".format(X_AXIS_LABELS[col],Y_AXIS_LABELS[row])

    def is_on_board(self, rowcol):
        row, col = rowcol
        return 0 <= row <= 7 and 0 <= col <= 7
