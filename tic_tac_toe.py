#!/usr/bin/env python3

from ttt.console_ui.consoleio import ConsoleIO
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Menu
from ttt.game.game_runner import GameRunner

consoleio = ConsoleIO()


def main():
    console = Console(consoleio)
    runner = GameRunner(console)
    menu = Menu(console, runner)

    menu.start()


if __name__ == '__main__':
    main()

