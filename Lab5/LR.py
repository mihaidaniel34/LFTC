from item import Item


class LR:
    def __init__(self, grammar):
        self.grammar = grammar
        grammar.augment()

    def closure(self, item):
        cls = [item]
        changed = True
        while changed:
            changed = False
            idx = 0
            while idx < len(cls):
                itm = cls[idx]
                if itm.dot_idx >= len(item.rhs):
                    idx += 1
                    continue
                non_terminal = itm.rhs[itm.dot_idx]
                if non_terminal not in self.grammar.non_terminals:
                    idx += 1
                    continue
                for prod in self.grammar.get_prod(non_terminal):
                    new_item = Item(non_terminal, prod, 0)
                    if new_item not in cls:
                        cls.append(new_item)
                        changed = True
                idx += 1
        return cls

    def goto(self, state, element):
        result = []
        for item in state:
            non_terminal = item.rhs[item.dot_idx]
            if non_terminal == element:
                next_item = Item(item.lhs, item.rhs, item.dot_idx + 1)
                result.append(self.closure(next_item))

        return result

    def get_after_dot(self, item):
        return item.rhs[item.dot_idx] if item.dot_idx < len(item.rhs) else None

    def dot_preceded_nt(self, items):
        return [self.get_after_dot(item) for item in items if self.get_after_dot(item) is not None]

    def canonical_collection(self):
        can_col = []
        can_col.append(
            self.closure(Item(self.grammar.starting_nt, self.grammar.get_prod(self.grammar.starting_nt)[0], 0)))
        idx = 0
        changed = True
        while changed:
            changed = False
            while idx < len(can_col):
                for sym in self.dot_preceded_nt(can_col[idx]):
                    goto_res = self.goto(can_col[idx], sym)[0]
                    if len(goto_res) > 0 and goto_res not in can_col:
                        changed = True
                        can_col.append(goto_res)
                idx += 1
        return can_col