from ttt.console_ui.consoleio import ConsoleIO
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Menu

consoleio = ConsoleIO()
console = Console(consoleio)
interface = Menu(console)


def main():
    interface.start()


if __name__ == '__main__':
    main()

