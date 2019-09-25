import os

# dict for notation equivalent char of pieces
pieces = {" #R ": "r", " #Kt ": "n", " #B ": "b", " #Q ": "q", " #K ": "k", " #P ": "p",
		  " ^R ": "R", " ^Kt ": "N", " ^B ": "B", " ^Q ": "Q", " ^K ": "K", " ^P ": "P", "    ": "1"}


# Turns the board info into notation, board only contains useful board rows (so 8 rows only)
def get_notation_form(board):
	notation = ""

	for line in board:
		row = ""
		for piece in line.split("|"):
			if piece in list(pieces.keys()):
				row += pieces[piece]

		notation = row + "/" + notation

	return notation


# starts to store the text when see the first dashed line, until it sees again, and ignores uninformative lines
# also writes the boards to text to check if the program works fine
def parse_text(f):
	board_parse = False
	board = []
	original_board_form = ""

	for line in f:
		if not board_parse:
			if line.strip() == "---------------------------------------":  #start of board
				original_board_form += line + "\n"
				board_parse = True

		else:
			original_board_form += line + "\n"
			if line.strip() == "---------------------------------------": #end of board
				board_parse = False

				with open(path_to_write, "a+") as f:
					notation_form = get_notation_form(board)
					notation_form += "\n\n####################################\n\n"
					f.write(original_board_form)
					f.write(notation_form)

				board = []
				original_board_form = ""

			elif line.strip() != "|---------------------------------------|": #uninformative line
				board.append(line.strip())


path_to_books = "/home/darg2/Desktop/books"
book1 = "Chess_Strategy_Edward_Lasker.txt"
book2 = "Chess_and_Checkers_The_Way_to_Mastership_by_Edward Lasker.txt"
path_to_write = "/home/darg2/Desktop/aa.txt"

file_handler = open(os.path.join(path_to_books, book1), "r", encoding="utf8")

parse_text(file_handler)

file_handler.close()


