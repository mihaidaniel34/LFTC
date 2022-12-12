class Grammar:
    def __init__(self, filename):
        self.starting_nt = ""
        self.non_terminals = []
        self.terminals = []
        self.productions = {}
        self.read_file(filename)

    def get_prod(self, nt):
        return self.productions[(nt,)]

    def augment(self):
        starting_symbol = "S0"
        if starting_symbol in self.non_terminals:
            return
        self.non_terminals.append(starting_symbol)
        self.productions[(starting_symbol,)] = [self.starting_nt]
        self.starting_nt = starting_symbol

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
