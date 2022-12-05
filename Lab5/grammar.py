class Grammar:
    def __init__(self, filename):
        self.starting_nt = ""
        self.non_terminals = []
        self.terminals = []
        self.productions = {}
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename) as f:
            self.non_terminals = f.readline().strip().split(" ")
            self.terminals = f.readline().strip().split(" ")
            self.starting_nt = f.readline().strip()
            for line in f:
                s_line = line.strip().split("->")
                self.productions.setdefault(tuple(s_line[0].strip().split(" ")), []).append(s_line[1].strip().split(" "))

    def cfg_check(self):
        return not any([elem for elem in self.productions.keys() if len(elem) > 1])

