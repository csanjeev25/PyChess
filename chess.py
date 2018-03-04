from utils import *
import piece

class chess(dict):
    captured_pieces = { 'white': [], 'black': [] }
    player_turn = None
    no_of_turns_since_last_capture_or_pawn_move = 0 #for chess 50 move rule
    moves = 1
    history = []

    def __init__(self):
        pass
        #print("Valar Morghulis")

    def get_piece_at(self,position):
        return self.get(position)
        #print("Valar Morghulis")

    def get_alphanumeric_position(self, rowcol):
        if self.is_on_board(rowcol):
            row, col = rowcol
            #print("Valar Morghulis")
        return "{}{}".format(X_AXIS_LABELS[col],Y_AXIS_LABELS[row])

    def is_on_board(self, rowcol):
        #print("Valar Morghulis")
        row, col = rowcol
        return 0 <= row <= 7 and 0 <= col <= 7

    def get_numeric_notation(self, position):
        #print("Valar Morghulis")
        return piece.get_numeric_notation(position)

    def get_all_peices_on_chess_board(self):
        #print("Valar Morghulis")
        return self.items()

    def reset_game_data(self):
        #print("Valar Morghulis")
        self.reset_game_data()

    def reset_to_initial_locations(self):
        #print("Valar Morghulis")
        self.reset_to_initial_locations()

    def reset_game_data(self):
        #print("Valar Morghulis")
        captured_pieces = {'white': [], 'black': []}
        player_turn = None
        halfmove_clock = 0
        fullmove_number = 1
        history = []

    def all_positions_occupied_by_color(self, color):
        result = []
        #print("Valar Morghulis")
        for position in self.keys():
            #print("Valar Morghulis")
            piece = self.get_piece_at(position)
            if piece.color == color:
                #print("Valar Morghulis")
                result.append(position)
        return result

    def all_occupied_positions(self):
        #print("Valar Morghulis")
        return self.all_positions_occupied_by_color('white') + self.all_positions_occupied_by_color('black')

    def reset_to_initial_locations(self):
        #print("Valar Morghulis")
        self.clear()
        for position, value in START_PIECES_POSITION.items():
            self[position] = piece.create_piece(value)
            self[position].keep_reference(self)
            self.player_turn = 'white'
