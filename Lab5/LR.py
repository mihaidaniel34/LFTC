from item import Item
from state import State, ACTION


class Link:
    def __init__(self, initial_state, final_state, symbol):
        self.initial_state = initial_state
        self.final_state = final_state
        self.symbol = symbol

    def __str__(self):
        return f"Link{self.initial_state} -> {self.final_state} & {self.symbol} "


class LR:
    def __init__(self, grammar):
        self.can_col = []
        self.grammar = grammar
        self.links = []
        grammar.augment()
        self.canonical_collection()
        self.parsing_table = {}

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
                    new_item = Item(non_terminal, prod[0], 0)
                    if new_item not in cls:
                        cls.append(new_item)
                        changed = True
                idx += 1
        return State(item, cls, self.grammar.enriched_sym)

    def goto(self, state, element):
        result = []
        for item in state.closure:
            non_terminal = item.rhs[item.dot_idx]
            if non_terminal == element:
                next_item = Item(item.lhs, item.rhs, item.dot_idx + 1)

                for st in self.can_col:
                    # print(st.items, next_item)
                    if st.items == next_item:
                        result.append(st)
                        break
                result.append(self.closure(next_item))
        return result

    def get_after_dot(self, item):
        return item.rhs[item.dot_idx] if item.dot_idx < len(item.rhs) else None

    def dot_preceded_nt(self, items):
        return [self.get_after_dot(item) for item in items.closure if self.get_after_dot(item) is not None]

    def canonical_collection(self):
        self.can_col = [
            self.closure(Item(self.grammar.starting_nt, self.grammar.get_prod(self.grammar.starting_nt)[0], 0))]
        idx = 0
        changed = True
        while changed:
            changed = False
            while idx < len(self.can_col):
                for sym in self.can_col[idx].get_all_after_dot():
                    goto_res = self.goto(self.can_col[idx], sym)[0]
                    if len(goto_res.closure) > 0 and goto_res not in self.can_col:
                        changed = True
                        self.can_col.append(goto_res)
                    self.links.append(Link(self.can_col[idx], goto_res, sym))
                idx += 1

    def get_state_links(self, state):
        return [link for link in self.links if link.initial_state == state]

    def get_prod_num(self, state):
        for prod in self.grammar.productions.keys():
            for prod_value in self.grammar.productions[prod]:
                if state.closure[0].lhs == prod[0] and state.closure[0].rhs == prod_value[0]:
                    return prod_value[1]
        return None

    def create_parsing_table(self):
        for state in self.can_col:
            links = self.get_state_links(state)
            if len(links) == 0:
                if state.action == ACTION.ACCEPT:
                    self.parsing_table[state.id] = (ACTION.ACCEPT, None)
                elif state.action == ACTION.REDUCE:
                    prod_id = self.get_prod_num(state)
                    if prod_id is None:
                        raise RuntimeError("Something went wrong!")
                    self.parsing_table[state.id] = (ACTION.REDUCE, prod_id)
            elif state.action == ACTION.SHIFT or state.action == ACTION.SHIFT_REDUCE_CONFLICT:
                if state.id not in self.parsing_table.keys():
                    self.parsing_table[state.id] = (state.action, {})
                for link in links:
                    self.parsing_table[state.id][1][link.symbol] = link.final_state.id
            else:
                if state.action == ACTION.REDUCE_REDUCE_CONFLICT:
                    raise RuntimeError("Reduce reduce conflict")
