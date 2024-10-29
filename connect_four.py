class ConnectFour:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = [['*' for _ in range(columns)] for _ in range(rows)]
        self.current_player = 'x'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def drop_piece(self, column):
        for row in reversed(self.board):
            if row[column] == '*':
                row[column] = self.current_player
                return True
        return False  # Column is full

    def check_winner(self):
        # Horizontal, vertical, and diagonal check methods here
        pass

    def switch_player(self):
        self.current_player = 'o' if self.current_player == 'x' else 'x'

    def play_turn(self, column):
        if self.drop_piece(column):
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                return True
            self.switch_player()
        else:
            print("Column is full. Choose another.")
        return False

def main():
    game = ConnectFour()
    game.print_board()
    # Placeholder for sample game turns
    # Example: game.play_turn(3)

if __name__ == "__main__":
    main()
