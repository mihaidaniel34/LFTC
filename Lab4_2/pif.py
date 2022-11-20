class Pif:
    def __init__(self):
        self.data = []

    def add(self, elem, pos):
        self.data.append((elem, pos))

    def __repr__(self):
        return "".join([elem[0] + ":" + f"({elem[1][0]}, {elem[1][1]})\n" for elem in self.data])

    def get_last(self):
        return self.data[-1]
