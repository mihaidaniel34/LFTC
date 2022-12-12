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

    def gotTo(self, state, element):
        result = []
        for item in state.items:
            nonTerminal = item.rhs[item.dot_idx]
            if nonTerminal == element:
                nextItem = Item(item.lhs, item.rhs, item.dot_idx + 1)
                result.append(nextItem)

        return result
