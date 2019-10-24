#!/usr/bin/env python
import signal
import sys

from ttt.console_ui.console import Console
from ttt.console_ui.consoleio import ConsoleIO
from ttt.console_ui.menu import Menu
from ttt.game.game_runner import GameRunner


consoleio = ConsoleIO()
console = Console(consoleio)
menu = Menu(console)
runner = GameRunner(console)


def main():
    signal.signal(signal.SIGINT, _exit)

    playing = True
    while playing:
        config = menu.configure_game()
        runner.run(config)
        playing = menu.play_again()


def _exit(sig, frame):
    menu.exit()
    runner.stop()
    sys.exit()


if __name__ == '__main__':
    main()
