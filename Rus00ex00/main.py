import sys
import os

def checkmate(board_str):
    try:
        board = board_str.strip().split('\n')
        size = len(board)
        if any(len(row) != size for row in board):
            return "Error"

        king_pos = None
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    break
            if king_pos:
                break

        if not king_pos:
            return "Error"

        xk, yk = king_pos

        diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pawn_attacks = [(-1, -1), (-1, 1)]

        for dx, dy in pawn_attacks:
            xp, yp = xk + dx, yk + dy
            if 0 <= xp < size and 0 <= yp < size:
                if board[xp][yp] == 'P':
                    return "Success"

        for dx, dy in diag_dirs:
            xi, yi = xk + dx, yk + dy
            while 0 <= xi < size and 0 <= yi < size:
                piece = board[xi][yi]
                if piece != '.':
                    if piece in 'BQ':
                        return "Success"
                    else:
                        break
                xi += dx
                yi += dy

        for dx, dy in straight_dirs:
            xi, yi = xk + dx, yk + dy
            while 0 <= xi < size and 0 <= yi < size:
                piece = board[xi][yi]
                if piece != '.':
                    if piece in 'RQ':
                        return "Success"
                    else:
                        break
                xi += dx
                yi += dy

        return "Fail"

    except Exception:
        return "Error"

def main():
    if len(sys.argv) < 2:
        print("Error")
        return

    for filename in sys.argv[1:]:
        if not os.path.isfile(filename):
            print("Error")
            continue
        try:
            with open(filename, 'r') as f:
                board_data = f.read()
                result = checkmate(board_data)
                print(result)
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()