#####################
# Welcome to Cursor #
#####################

'''
Step 1: Try generating with Cmd+K or Ctrl+K on a new line. Ask for CLI-based game of TicTacToe.

Step 2: Hit Cmd+L or Ctrl+L and ask the chat what the code does. 
   - Then, try running the code

Step 3: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
   - Instruct it to change the game in some way (e.g. add colors, add a start screen, make it 4x4 instead of 3x3)

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
'''
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

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

def get_empty_positions(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def start_screen():
    print("################################")
    print("# 三目並べへようこそ！          #")
    print("# 'X' と 'O' でプレイします。 #")
    print("# ゲームのルール:              #")
    print("# 3x3のグリッドに 'X' または 'O' を配置します。#")
    print("# 同じ記号が縦、横、または斜めに3つ並ぶと勝ちです。#")
    print("# ゲームを開始するには何かキーを押してください。 #")
    print("################################")
    input()

def tictactoe():
    start_screen()
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        empty_positions = get_empty_positions(board)
        if not empty_positions:
            print("引き分けです！")
            break
        print(f"{current_player}の番です。")
        row, col = map(int, input("行と列をスペースで区切って入力してください (例: 1 2): ").split())
        if (row, col) in empty_positions:
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"おめでとうございます！ {current_player}の勝ちです！")
                break
            current_player = "X" if current_player == "O" else "O"
        else:
            print("無効な入力です。もう一度入力してください。")

if __name__ == "__main__":
    tictactoe()
