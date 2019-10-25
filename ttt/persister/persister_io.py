class PersisterIO:
    def write(self, filename, content):
        file = open(filename, "w+")
        file.write(content)
        file.close()

    def read(self, filename):
        file = open(filename, "r")
        return file.read()
