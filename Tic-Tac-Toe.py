import tkinter as tk
from tkinter import messagebox

# Constants
EMPTY = ""
X_PLAYER = "X"
O_PLAYER = "O"

def print_board(board):
    # Function to display the current state of the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))  # Joins elements of the row with " | "
        print("-" * 9)  # Prints horizontal line to separate rows

def check_winner(board):
    # Function to check if there's a winner on the board
    if _check_rows(board) or _check_columns(board) or _check_diagonals(board):
        return True
    return False

def _check_rows(board):
    # Helper function to check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return True
    return False

def _check_columns(board):
    # Helper function to check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return True
    return False

def _check_diagonals(board):
    # Helper function to check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    return False

def is_board_full(board):
    # Function to check if the board is full
    for row in board:
        if EMPTY in row:
            return False
    return True

def restart_game(result_label):
    global board, current_player
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = X_PLAYER
    update_board_ui()
    result_label.config(text=f"Player {current_player}'s turn")

def update_board_ui():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

def play_game():
    # Function to start and manage the Tic-Tac-Toe game
    global board, current_player, buttons

    # Initialize game variables
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = X_PLAYER

    # Create a new window
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    # Function to handle button clicks
    def button_click(row, col):
        global current_player
        if board[row][col] == EMPTY:
            board[row][col] = current_player
            buttons[row][col].config(text=current_player)
            if check_winner(board):
                print_board(board)
                messagebox.showinfo("Game Over", f"Player {current_player} wins!")
                restart_game(result_label)
            elif is_board_full(board):
                print_board(board)
                messagebox.showinfo("Game Over", "It's a tie!")
                restart_game(result_label)
            else:
                current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER
                result_label.config(text=f"Player {current_player}'s turn")

    # Create buttons for the Tic-Tac-Toe grid
    buttons = []
    for i in range(3):
        row_buttons = []
        for j in range(3):
            button = tk.Button(root, text="", width=6, height=3, command=lambda row=i, col=j: button_click(row, col))
            button.grid(row=i, column=j)
            row_buttons.append(button)
        buttons.append(row_buttons)

    result_label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 12))
    result_label.grid(row=3, columnspan=3)

    restart_button = tk.Button(root, text="Restart", command=lambda: restart_game(result_label))
    restart_button.grid(row=4, columnspan=3)

    root.mainloop()

# Start the game
play_game()
