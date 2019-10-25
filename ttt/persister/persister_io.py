from os import path

class PersisterIO:
    def write(self, filename, content):
        file = open(filename, "w+")
        file.write(content)
        file.close()

    def read(self, filename):
        if not path.exists(filename):
            self.write(filename, '')
        file = open(filename, "r")
        return file.read()
