from chess_utils import *
from tkinter import *

class Chess_GUI(dict):
    def __init__(self,window):
        self.window=window
        self.BOARD_COLOR_1 = BOARD_COLOR_1
        self.BOARD_COLOR_2 = BOARD_COLOR_2
        self.create_chess_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)

    def on_square_clicked(self, event):
        clicked_row, clicked_column =self.get_clicked_row_column(event)
        print("Hey you clicked on", clicked_row, clicked_column)

    def get_clicked_row_column(self, event):
        col_size = row_size = DIMENSION_OF_EACH_SQUARE
        clicked_column = event.x // col_size
        clicked_row = 7 - (event.y // row_size)
        return (clicked_row, clicked_column)

    def create_chess_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        self.create_bottom_frame()

    def create_top_menu(self):
        self.menubar = Menu(window)
        self.filemenu = Menu(self.menubar, tearoff=0 )
        self.filemenu.add_command(label="New Game", command=self.new_game )
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.window.config(menu=self.menubar)

    def new_game(self):
        pass

    def create_canvas(self):
        canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        self.canvas = Canvas(self.window, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)

    def draw_board(self):
        color = self.BOARD_COLOR_2
        for row in range(NUMBER_OF_ROWS):
            color = self.get_alternate_color(color)
            for col in range(NUMBER_OF_COLUMNS):
                x1 = (col * DIMENSION_OF_EACH_SQUARE)
                y1 = ((7-row) * DIMENSION_OF_EACH_SQUARE)
                x2 = x1 + DIMENSION_OF_EACH_SQUARE
                y2 = y1 + DIMENSION_OF_EACH_SQUARE
                self.canvas.create_rectangle(x1, y1, x2, y2,  fill=color, tags="area")
                color = self.get_alternate_color(color)

    def get_alternate_color(self, current_color):
        if current_color == self.BOARD_COLOR_2:
            next_color = self.BOARD_COLOR_1
        else:
            next_color = self.BOARD_COLOR_2
        return next_color

    def get_x_y_coordinate(self,row,col):
        x=(col*DIMENSION_OF_EACH_SQUARE)
        y=((7-x)*DIMENSION_OF_EACH_SQUARE)
        return(x,y)

    def create_bottom_frame(self):
        self.bottom_frame = Frame(window, height=64)
        self.info_label = Label(self.bottom_frame, text="   White to Start the Game  ", fg=self.BOARD_COLOR_2)
        self.info_label.pack(side=RIGHT, padx=8, pady=5)
        self.bottom_frame.pack(fill="x", side=BOTTOM)

if __name__ == "__main__":
    window = Tk()
    window.title("Chess")
    gui = Chess_GUI(window)
    window.mainloop()
