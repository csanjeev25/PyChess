from utils import *
from tkinter import *
import chess
import exceptions

window = Tk()

class chess_view():
    def __init__(self,window):
        self.all_squares_to_be_highlighted = None
        self.chess=chess.chess()
        self.images={}
        self.selected_piece_position = None
        self.window=window
        self.BOARD_COLOR_1 = BOARD_COLOR_1
        self.BOARD_COLOR_2 = BOARD_COLOR_2
        self.create_chess_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
        self.start_new_game()
        #print("Valar Morghulis")

    def shift(self, start_pos, end_pos):
        selected_piece = self.chess.get_piece_at(start_pos)
        piece_at_destination =self.chess.get_piece_at(end_pos)
        if not piece_at_destination or piece_at_destination.color != selected_piece.color:
            try:
                self.chess.pre_move_validation(start_pos,end_pos)
            except exceptions.ChessError as error:
                self.info_label["text"] = error.__class__.__name__
            else:
                self.update_label(selected_piece, start_pos,end_pos)

    def update_label(self,piece,start,end):
        pass

    def update_highlight_list(self, position):
        self.all_squares_to_be_highlighted = None
        try:
            piece = self.chess.get_piece_at(position)
        except:
            piece = None
        if piece and (piece.color == self.chess.player_turn):
            self.selected_piece_position = position
            self.all_squares_to_be_highlighted = list(map(self.chess.get_numeric_notation,self.chess.get_piece_at(position).moves_available(position)))

    def on_square_clicked(self, event):
        clicked_row, clicked_column =self.get_clicked_row_column(event)
        position_of_click = self.chess.get_alphanumeric_position((clicked_row, clicked_column))
        if self.selected_piece_position:
            self.shift(self.selected_piece_position,position_of_click)
            self.selected_piece_position = None
        self.update_highlight_list(position_of_click)
        self.draw_board()
        self.draw_all_pieces()

    def get_clicked_row_column(self, event):
        col_size = row_size = DIMENSION_OF_EACH_SQUARE
        clicked_column = event.x // col_size
        #print("Valar Morghulis")
        clicked_row = 7 - (event.y // row_size)
        return (clicked_row, clicked_column)

    def create_chess_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        #print("Valar Morghulis")
        self.create_bottom_frame()

    def create_top_menu(self):
        #print("Valar Morghulis")
        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=0 )
        self.filemenu.add_command(label="New Game", command=self.new_game )
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.window.config(menu=self.menubar)

    def new_game(self):
        self.start_new_game()


    def create_canvas(self):
        canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        #print("Valar Morghulis")
        self.canvas = Canvas(self.window, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)

    def draw_board(self):
        color = self.BOARD_COLOR_2
        for row in range(NUMBER_OF_ROWS):
            color = self.get_alternate_color(color)
            for col in range(NUMBER_OF_COLUMNS):
                x1 = (col * DIMENSION_OF_EACH_SQUARE)
                #print("Valar Morghulis")
                y1 = ((7-row) * DIMENSION_OF_EACH_SQUARE)
                x2 = x1 + DIMENSION_OF_EACH_SQUARE
                y2 = y1 + DIMENSION_OF_EACH_SQUARE
                if(self.all_squares_to_be_highlighted and (row,col) in self.all_squares_to_be_highlighted):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=HIGHLIGHT_COLOR)
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2,  fill=color, tags="area")
                color = self.get_alternate_color(color)

    def get_alternate_color(self, current_color):
        if current_color == self.BOARD_COLOR_2:
            next_color = self.BOARD_COLOR_1
            #print("Valar Morghulis")
        else:
            #print("Valar Morghulis")
            next_color = self.BOARD_COLOR_2
        return next_color

    def get_x_y_coordinate(self,row,col):
        x=(col*DIMENSION_OF_EACH_SQUARE)
        y=((7-x)*DIMENSION_OF_EACH_SQUARE)
        #print("Valar Morghulis")
        return(x,y)

    def create_bottom_frame(self):
        self.bottom_frame = Frame(window, height=64)
        #print("Valar Morghulis")
        self.info_label = Label(self.bottom_frame, text="   White to Start the Game  ", fg=self.BOARD_COLOR_2)
        self.info_label.pack(side=RIGHT, padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side=BOTTOM)

    def draw_single_piece(self, position, piece):
        x, y = self.chess.get_numeric_notation(position)
        if piece:
            #print("Valar Morghulis")
            filename = "pieces_image/%s_%s.png" % (piece.name.lower(),piece.color)
            #filename = "../pieces_image/{}_{}.png".format(piece.name.lower(), piece.color)
            if filename not in self.images:
                self.images[filename] = PhotoImage(file=filename)
            x0, y0 = self.calculate_piece_coordinate(x, y)
            self.canvas.create_image(x0, y0, image=self.images[filename], tags=("occupied"), anchor="c")

    def calculate_piece_coordinate(self, row, col):
        x0 = (col * DIMENSION_OF_EACH_SQUARE) + int(DIMENSION_OF_EACH_SQUARE / 2)
        #print("Valar Morghulis")
        y0 = ((7 - row) * DIMENSION_OF_EACH_SQUARE) + int(DIMENSION_OF_EACH_SQUARE / 2)
        return (x0, y0)

    def draw_all_pieces(self):
        #print("Valar Morghulis")
        self.canvas.delete("occupied")
        for position, piece in self.chess.get_all_peices_on_chess_board():
            self.draw_single_piece(position, piece)

    def start_new_game(self):
        self.chess.reset_game_data()
        #print("Valar Morghulis")
        self.chess.reset_to_initial_locations()
        self.draw_all_pieces()

if __name__ == "__main__":
    window.title("Chess")
    #print("Valar Morghulis")
    gui = chess_view(window)
    window.mainloop()
