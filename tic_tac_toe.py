#!/usr/bin/env python
import signal
import sys

from ttt.console_ui.consoleio import ConsoleIO
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Menu
from ttt.game.game_runner import GameRunner
from ttt.messages import end_game_message

consoleio = ConsoleIO()
console = Console(consoleio)


def main():
    signal.signal(signal.SIGINT, _signal_handler)

    runner = GameRunner(console)
    menu = Menu(console)

    playing = True
    while playing:
        config = menu.configure_game()
        runner.run(config)
        playing = menu.play_again()


def _signal_handler(sig, frame):
    _exit()


def _exit():
    console.clear_output()
    console.output_message(end_game_message())
    sys.exit()


if __name__ == '__main__':
    main()
