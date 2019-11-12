#!/usr/bin/env python
import signal
import sys

from ttt.console_ui.console import Console
from ttt.console_ui.consoleio import ConsoleIO
from ttt.console_ui.menu import Menu
from ttt.game.game_runner import GameRunner
from ttt.game.networked_game_runner import NetworkedGameRunner

consoleio = ConsoleIO()
console = Console(consoleio)
menu = Menu(console)
game_runner = GameRunner(console)


def main():
    signal.signal(signal.SIGINT, _exit)

    playing = True
    runner = game_runner

    while playing:
        config = menu.start()
        if config.server:
            runner = NetworkedGameRunner()
        runner.run(config)
        playing = menu.play_again()


def _exit(sig, frame):
    menu.exit()
    game_runner.stop()
    sys.exit()


if __name__ == '__main__':
    main()
