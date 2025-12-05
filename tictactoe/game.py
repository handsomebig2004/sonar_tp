from dataclasses import dataclass, field
from typing import List, Tuple, Literal
Player = Literal[0, 1, 2]

@dataclass
class Game:
    board: List[List[int]] = field(
        default_factory=lambda: [[0 for _ in range(3)] for _ in range(3)]
    )

    def reset(self) -> None:
        """reset the board"""
        for i in range(3):
            for j in range(3):
                self.board[i][j] = 0

    def move(self, next_move: Tuple[int, int], player: int) -> bool:
        """
        put a move on the board
        param:
            next_move: (row, col) in 0~2
            player: 0 represent remove move, 1 represent X, 2 represent O
        return: if move success return True，else False
        """
        r, c = next_move
        if not (0 <= r < 3 and 0 <= c < 3):
            return False

        if player not in (0, 1, 2):
            return False
        if player == 0:
            self.board[r][c] = 0
            return True
        
        if self.board[r][c] != 0:
            return False

        self.board[r][c] = player
        return True

    def check_finish(self) -> int:
        """
        check the game has finished
        return: -1:not finish, 0: draw, 1:player 1 wins, 2:player 2 wins
        """
        b = self.board

        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != 0:
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != 0:
                return b[0][i]
        if b[0][0] == b[1][1] == b[2][2] != 0:
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != 0:
            return b[0][2]

        if all(cell != 0 for row in self.board for cell in row):
            return 0
        
        return -1

    def __str__(self):
        symbol = {0: " ", 1: "X", 2: "O"}
        str_board = "-----\n"
        for i in range(3):
            str_board = str_board + "|".join(symbol[self.board[i][j]] for j in range(3)) + "\n-----\n"
            
        str_board = str_board + "————————————————————"

        return str_board
    

def main() -> None:
    game = Game()
    while game.check_finish() == -1:
        print(game)
        next_move = input("next move (row col player): ").split()
        if not game.move((int(next_move[0]), int(next_move[1])), int(next_move[2])):
            print("invalid move")
    print(game)
    winner = game.check_finish()
    if winner == 0:
        print("draw")
    else:
        print(f"player {winner} wins")


if __name__ == "__main__":
    main()


