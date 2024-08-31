import tkinter as tk
from tkinter import messagebox

current_player = "X"  # グローバル変数として定義

def print_board(board, buttons):
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])
    root.title(f"三目並べ - 次のプレイヤー: {current_player}")

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def on_button_click(r, c, board, buttons):
    global current_player
    if board[r][c] == " ":
        board[r][c] = current_player
        if check_winner(board, current_player):
            print_board(board, buttons)
            messagebox.showinfo("ゲーム終了", f"おめでとうございます！ {current_player}の勝ちです！")
            root.destroy()
        elif not any(" " in row for row in board):
            messagebox.showinfo("ゲーム終了", "引き分けです！")
            root.destroy()
        else:
            current_player = "X" if current_player == "O" else "O"
            print_board(board, buttons)

def tictactoe_gui():
    global root
    root = tk.Tk()
    root.title("三目並べ - 次のプレイヤー: X")
    board = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            cmd = lambda r=i, c=j: on_button_click(r, c, board, buttons)
            buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, command=cmd)
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    tictactoe_gui()