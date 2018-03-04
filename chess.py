from utils import *
import piece
import exceptions
from copy import deepcopy

class chess(dict):
    captured_pieces = { 'white': [], 'black': [] }
    player_turn = None
    no_of_turns_since_last_capture_or_pawn_move = 0 #for chess 50 move rule
    moves = 1
    history = []

    def move(self, start_pos, final_pos):
        self[final_pos] = self.pop(start_pos, None)

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

    def pre_move_validation(self, initial_pos, final_pos):
        initial_pos, final_pos = initial_pos.upper(),final_pos.upper()
        piece = self.get_piece_at(initial_pos)
        try:
            piece_at_destination = self.get_piece_at(final_pos)
        except:
            piece_at_destination = None
        if self.player_turn != piece.color:
            raise exceptions.NotYourTurn("Not " + piece.color +"'s turn!")
        enemy = ('white' if piece.color == 'black' else 'black')
        moves_available = piece.moves_available(initial_pos)
        if final_pos not in moves_available:
            raise exceptions.InvalidMove
        if self.get_all_available_moves(enemy):
            if self.will_move_cause_check(initial_pos, final_pos):
                raise exceptions.Check
            if not moves_available and self.is_king_under_check(piece.color):
                raise exceptions.CheckMate
            elif not moves_available:
                raise exceptions.Draw
            else:
                self.move(initial_pos, final_pos)
                self.update_game_statistics(piece, piece_at_destination, initial_pos,final_pos)
                self.change_player_turn(piece.color)

    def update_game_statistics(self,piece,dest,ini,final):
        pass

    def change_player_turn(self,color):
        pass

    def will_move_cause_check(self, start_position, end_position):
        tmp = deepcopy(self)
        tmp.move(start_position, end_position)
        return tmp.is_king_under_check(self[start_position].color)

    def get_alphanumeric_position_of_king(self, color):
        for position in self.keys():
            this_piece = self.get_piece_at(position)
            if isinstance(this_piece, piece.King) and this_piece.color == color:
                return position

    def is_king_under_check(self, color):
        position_of_king =self.get_alphanumeric_position_of_king(color)
        opponent = 'black' if color =='white' else 'white'
        return position_of_king in self.get_all_available_moves(opponent)

    def get_all_available_moves(self, color):
        result = []
        #print("Valar Morghulis")
        for position in self.keys():
            #print("Valar Morghulis")
            piece = self.get_piece_at(position)
            if piece and piece.color == color:
                #print("Valar Morghulis")
                moves = piece.moves_available(position)
                if moves:
                    #print("Valar Morghulis")
                    result.extend(moves)
        return result
