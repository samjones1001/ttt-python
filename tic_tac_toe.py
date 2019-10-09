from ttt.console_ui.consoleio import ConsoleIO
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Menu
from ttt.game.game_runner import GameRunner

consoleio = ConsoleIO()
console = Console(consoleio)
runner = GameRunner(console)
menu = Menu(console, runner)


def main():
    menu.start()


if __name__ == '__main__':
    main()

