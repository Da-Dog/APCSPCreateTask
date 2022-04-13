from colorama import Fore
from colorama import init as colorama_init
from art import text2art
from click import clear
import numpy

colorama_init(autoreset=True)


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
                        y_line += f"| {Fore.LIGHTRED_EX}X{Fore.RESET} | "
                    elif x == 2:
                        y_line += f"| {Fore.LIGHTBLUE_EX}X{Fore.RESET} | "
                print(y_line)
                y += 1
        for i in range(7):
            print(f"{Fore.LIGHTGREEN_EX}  {i + 1}   ", end="")

    def drop(self, column: int):
        column -= 1
        if column > 6:
            return
        for index, val in enumerate(reversed(self.board[:, column])):
            if val == 0:
                self.board[5 - index, column] = self.currentPlayer
                if self.currentPlayer == 1:
                    self.currentPlayer = 2
                else:
                    self.currentPlayer = 1
                break


if __name__ == '__main__':
    print(text2art("Welcome  to...", font="small"))
    print(text2art("CONNECT  4", font="small"))
    input(f'\n\n{Fore.LIGHTRED_EX}Click enter to start.')
    game = Connect4()
    while True:  # TODO: true should replace with ifWinner()
        clear()
        print(f"\n\n")
        game.print_board()
        print("\n")
        try:
            game.drop(int(input(f"{Fore.LIGHTRED_EX if game.currentPlayer == 1 else Fore.LIGHTBLUE_EX}Player "
                                f"{game.currentPlayer}{Fore.RESET}, Please enter your next step... ")))
        except ValueError:
            pass
