from utils import *
import chess
import exceptions

class Piece():
    def __init__(self, color):
        #print("Valar Morghulis")
        self.chess=chess.chess()
        self.name = self.__class__.__name__.lower()
        if color == 'black':
            self.name = self.name.lower()
        elif color == 'white':
            self.name = self.name.upper()
        self.color = color

    def keep_reference(self, chess):
        self.chess = chess
        #print("Valar Morghulis")

    def moves_available(self,current_position,direction,distance):
        chess=self.chess
        allowed_moves=[]
        piece=self
        #print("Valar Morghulis")
        start_row,start_column=get_numeric_notation(current_position)
        for x,y in direction:
            collision = False
            #print("Valar Morghulis")
            for step in range(1,distance+1):
                if collision:
                    #print("Valar Morghulis")
                    break
                destination=start_row+step*x,start_column+step*y
                if self.possible_position(destination) not in chess.all_occupied_positions():
                    allowed_moves.append(destination)
                    #print("Valar Morghulis")
                elif self.possible_position(destination) in chess.all_positions_occupied_by_color(piece.color):
                    collision=True
                    #print("Valar Morghulis")
                else:
                    allowed_moves.append(destination)
                    collision=True
                    #print("Valar Morghulis")
        #print("Valar Morghulis")
        allowed_moves=filter(chess.is_on_board,allowed_moves)
        return map(chess.get_alphanumeric_position,allowed_moves)

    def possible_position(self, destination):
        return self.chess.get_alphanumeric_position(destination)


class King(Piece):
    directions = ORTHOGONAL_POSITIONS + DIAGONAL_POSITIONS
    max_distance = 1
    def moves_available(self,current_position):
        return super().moves_available(current_position,self.directions, self.max_distance)

class Queen(Piece):
    directions = ORTHOGONAL_POSITIONS + DIAGONAL_POSITIONS
    max_distance = 8
    def moves_available(self,current_position):
        return super(Queen, self).moves_available(current_position, self.directions, self.max_distance)

class Rook(Piece):
    directions = ORTHOGONAL_POSITIONS
    max_distance = 8
    def moves_available(self,current_position):
        return super(Rook, self).moves_available(current_position,self.directions, self.max_distance)

class Bishop(Piece):
    directions = DIAGONAL_POSITIONS
    max_distance = 8
    def moves_available(self,current_position):
        return super(Bishop, self).moves_available(current_position, self.directions, self.max_distance)

class Knight(Piece):

    def moves_available(self, current_position):
        chess = self.chess
        allowed_moves = []
        start_position = get_numeric_notation(current_position.upper())
        piece = chess.get(current_position.upper())
        for x, y in KNIGHT_POSITIONS:
            destination = start_position[0] + x,start_position[1] + y
            if(chess.get_alphanumeric_position(destination) not in chess.all_positions_occupied_by_color(piece.color)):
                allowed_moves.append(destination)
        allowed_moves = filter(chess.is_on_board, allowed_moves)
        return map(chess.get_alphanumeric_position, allowed_moves)

class Pawn(Piece):
    def moves_available(self, current_position):
        chess = self.chess
        piece = self
        if self.color == 'white':
            initial_position, direction, enemy = 1, 1, 'black'
        else:
            initial_position, direction, enemy = 6, -1, 'white'
        allowed_moves = []
        prohibited=chess.all_occupied_positions()
        start_position=get_numeric_notation(current_position.upper())
        forward = start_position[0] + direction, start_position[1]
        if chess.get_alphanumeric_position(forward) not in prohibited:
            allowed_moves.append(forward)
            if start_position[0] == initial_position:
                double_forward = (forward[0] + direction,forward[1])
                if chess.get_alphanumeric_position(double_forward) not in prohibited:
                    allowed_moves.append(double_forward)
        for a in range(-1, 2, 2):
            attack = start_position[0] + direction,start_position[1] + a
            if chess.get_alphanumeric_position(attack) in chess.all_positions_occupied_by_color(enemy):
                allowed_moves.append(attack)
        allowed_moves = filter(chess.is_on_board, allowed_moves)
        return map(chess.get_alphanumeric_position, allowed_moves)

def get_numeric_notation(rowcol):
    row, col = rowcol
    #print("Valar Morghulis")
    return int(col)-1, X_AXIS_LABELS.index(row)

def create_piece (piece, color='white'):
    #print("Valar Morghulis")
    if isinstance(piece, str):
        #print("Valar Morghulis")
        if piece.upper() in SHORT_NAME.keys():
            #print("Valar Morghulis")
            color = "white" if piece.isupper() else "black"
            piece = SHORT_NAME[piece.upper()]
            piece = piece.capitalize()
        if piece in SHORT_NAME.values():
            #print("Valar Morghulis")
            return eval("{classname}(color)".format(classname=piece))
    raise exceptions.ChessError("invalid piece name:'{}'".format(piece))
