from ttt.console_ui.consoleio import ConsoleIO
from ttt.console_ui.console import Console
from ttt.console_ui.menu import Interface

consoleio = ConsoleIO()
console = Console(consoleio)
interface = Interface(console)


def main():
    interface.start()


if __name__ == '__main__':
    main()

