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
        for index, val in enumerate(reversed(self.board[:, column])):
            if val == 0:
                self.board[5 - index, column] = self.currentPlayer
                if self.currentPlayer == 1:
                    self.currentPlayer = 2
                else:
                    self.currentPlayer = 1
                break


def main_menu():
    print(text2art("Welcome  to...", font="small"))
    print(text2art("CONNECT  4", font="small"))
    print(f"{Fore.LIGHTRED_EX}1. PVP, 2. AI, 3. Quit")
    while True:
        game_choice = input('Choose the game mode (Default PVP)  [1]: ')
        if game_choice == "1" or not game_choice:
            return 0
        elif game_choice == "2":
            return 1
        elif game_choice == "3":
            exit(0)


if __name__ == '__main__':
    game_mode = main_menu()  # 0 PVP, 1 AI
    game = Connect4()
    while True:  # TODO: true should replace with ifWinner()
        clear()
        print(f"Current Game Mode: {Fore.GREEN}" + "PVP \n" if game_mode == 0 else "AI \n")
        game.print_board()
        print("\n")
        try:
            game.drop(int(input(f"{Fore.LIGHTRED_EX if game.currentPlayer == 1 else Fore.LIGHTBLUE_EX}Player "
                                f"{game.currentPlayer}{Fore.RESET}, Please enter your next step... ")))
        except ValueError:
            pass
