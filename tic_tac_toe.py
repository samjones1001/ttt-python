from ttt.consoleio import ConsoleIO
from ttt.console import Console
from ttt.interface import Interface

consoleio = ConsoleIO()
console = Console(consoleio)
interface = Interface(console)


def main():
    interface.start()


if __name__ == '__main__':
    main()

