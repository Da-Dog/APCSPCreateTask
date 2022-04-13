from colorama import Fore
from colorama import init as colorama_init
from art import text2art
from click import clear
import numpy

colorama_init(autoreset=True)


def if_connect_4(row):
    counter = 0
    counting_player = 0
    for x in row:
        if x != 0 and counting_player == x:
            counting_player = x
            counter += 1
        elif x != 0:
            counter = 1
            counting_player = x
        else:
            counter = 0
            counting_player = 0
        if counter >= 4:
            clear()
            print(f"\n{Fore.RED if counting_player == 1 else Fore.BLUE}Player {int(counting_player)}"
                  f"{Fore.RESET} Win!\n")
            return True
    return False


class Connect4:
    board = numpy.zeros([6, 7])  # 0 empty, 1 red, 2 blue
    currentPlayer = 1  # 1 red, 2 blue

    def print_board(self):
        y = 0
        for i in range(13):
            if i % 2 == 0:
                print("- - - " * 7)
            else:
                y_line = ""
                for x in self.board[y]:
                    if x == 0:
                        y_line += "|   | "
                    elif x == 1:
                        y_line += f"| {Fore.RED}X{Fore.RESET} | "
                    elif x == 2:
                        y_line += f"| {Fore.BLUE}X{Fore.RESET} | "
                print(y_line)
                y += 1
        for i in range(7):
            print(f"{Fore.LIGHTGREEN_EX}  {i + 1}   ", end="")

    def drop(self, column: int):
        column -= 1
        if 6 < column or column < 0:
            return
        for index, val in enumerate(reversed(self.board[:, column])):
            if val == 0:
                self.board[5 - index, column] = self.currentPlayer
                if self.currentPlayer == 1:
                    self.currentPlayer = 2
                else:
                    self.currentPlayer = 1
                break

    def if_winner(self):
        if 0 not in self.board:
            clear()
            print(f"\nDraw!\n")
            self.print_board()
            return False
        for i in range(6):
            if if_connect_4(self.board[:, i]):
                self.print_board()
                return False
        for y in self.board:
            if if_connect_4(y):
                self.print_board()
                return False
        for diag in range(-2, 4):
            if if_connect_4(self.board.diagonal(diag)):
                self.print_board()
                return False
        for diag in range(-2, 4):
            if if_connect_4(numpy.fliplr(self.board).diagonal(diag)):
                self.print_board()
                return False
        return True

    def restart(self):
        self.board = numpy.zeros([6, 7])
        self.currentPlayer = 1


if __name__ == '__main__':
    print(text2art("Welcome  to...", font="small"))
    print(text2art("CONNECT  4", font="small"))
    input(f'\n\n{Fore.LIGHTRED_EX}Click enter to start... ')
    game = Connect4()
    while True:
        game.restart()
        while game.if_winner():
            clear()
            print(f"\n")
            game.print_board()
            print("\n")
            try:
                game.drop(int(input(f"{Fore.RED if game.currentPlayer == 1 else Fore.BLUE}Player "
                                    f"{game.currentPlayer}{Fore.RESET}, Please enter your next step... ")))
            except ValueError:
                pass
        if input("\n\nDo you want to play again? (y/n) ") != "y":
            exit(0)
