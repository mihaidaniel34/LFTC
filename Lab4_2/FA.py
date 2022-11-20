class FA:
    def __init__(self, filename):
        self.states = []
        self.alphabet = []
        self.transition = {}
        self.initial_state = ""
        self.final_states = []
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename) as f:
            self.states = f.readline().strip().replace(" ", "").split(",")
            if len(self.states) == 0:
                raise RuntimeError("Error while parsing states")
            self.alphabet = f.readline().strip().replace(" ", "").split(",")
            if len(self.alphabet) == 0:
                raise RuntimeError("Error while parsing alphabet")
            self.initial_state = f.readline().strip()
            if len(self.initial_state) == 0:
                raise RuntimeError("Error while parsing initial state")
            self.final_states = f.readline().strip().replace(" ", "").split(",")
            if len(self.final_states) == 0:
                raise RuntimeError("Error while parsing final states")
            for read_line in f:
                line = read_line.strip().replace(" ", "").split("=")
                pair = line[0].strip().split(",")
                if len(pair) != 2 or len(line) == 0:
                    raise RuntimeError("Error while parsing transition functions")
                self.transition.setdefault((pair[0], pair[1]), []).append(line[1])

    def deterministic(self):
        return False if any([elem for elem in self.transition.values() if len(elem) > 1]) else True

    def check_sequence(self, sequence):
        if self.deterministic():
            state = self.initial_state
            for path in sequence:
                if (state, str(path)) not in self.transition.keys():
                    return False
                state = self.transition[(state, str(path))][0]
            return state in self.final_states
        return False

    def get_accepted(self, seq):
        state = self.initial_state

        accepted = ""
        for path in seq:
            if (state, str(path)) not in self.transition.keys():
                break
            state = self.transition[(state, str(path))][0]
            accepted += path
        return accepted

    def __repr__(self):
        return " States:  " + str(self.states) + "\n Alphabet: " + str(
            self.alphabet) + "\n Transition Functions: " + str(
            self.transition) + "\n Initial state: " + self.initial_state + "\n Final states: " + str(self.final_states)
