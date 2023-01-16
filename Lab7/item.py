class Item:
    def __init__(self, lhs, rhs, dot_idx):
        self.lhs = lhs
        self.rhs = rhs
        self.dot_idx = dot_idx

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.lhs == other.lhs and self.rhs == other.rhs and self.dot_idx == other.dot_idx

        return False

    def __repr__(self):
        # return f"{self.lhs} -> {''.join(''.join(self.rhs)[:self.dot_idx])}.{''.join(''.join(self.rhs)[self.dot_idx:])}"
        return str(self.lhs) + " -> " + " ".join(self.rhs[:self.dot_idx]) + "." + " ".join(self.rhs[self.dot_idx:])
