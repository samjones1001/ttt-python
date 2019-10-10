from os import system


class ConsoleIO:
    def get_input(self, message=""):
        return input()

    def print_output(self, output):
        print(output)

    def clear(self):
        system('clear')

