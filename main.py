from colorama import Fore
from colorama import init as colorama_init
from art import text2art
from sys import exit
from click import clear
import numpy

colorama_init(autoreset=True)


class Connect4:
    board = numpy.zeros([6, 7])  # 0 empty, 1 red, 2 blue

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
    clear()
    game = Connect4()
    print(f"Current Game Mode: {Fore.GREEN}" + "PVP" if game_mode == 0 else "AI")
    print("")
    game.print_board()
