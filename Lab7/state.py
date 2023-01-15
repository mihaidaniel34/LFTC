import itertools
from enum import Enum


class ACTION(Enum):
    SHIFT = 1
    ACCEPT = 2
    REDUCE = 3
    REDUCE_REDUCE_CONFLICT = 4
    SHIFT_REDUCE_CONFLICT = 5


class State:

    id = itertools.count()

    def __init__(self, items, closure, enriched_symbol):
        self.action = None
        self.id = next(self.id)
        self.items = items
        self.closure = closure
        self.set_action(enriched_symbol)

    def set_action(self, enriched_symbol):
        if len(self.closure) == 1 and len(self.closure[0].rhs) == self.closure[0].dot_idx \
                and self.closure[0].lhs == enriched_symbol:
            self.action = ACTION.ACCEPT
        elif len(self.closure) == 1 and self.closure[0].dot_idx == len(self.closure[0].rhs):
            self.action = ACTION.REDUCE
        elif len(self.closure) != 0 and self.check_doesnt_end_in_dot():
            self.action = ACTION.SHIFT
        else:
            if len(self.closure) != 0 and self.check_ends_in_dot():
                self.action = ACTION.REDUCE_REDUCE_CONFLICT
            else:
                self.action = ACTION.SHIFT_REDUCE_CONFLICT

    def check_ends_in_dot(self):
        for item in self.closure:
            if len(item.rhs) > item.dot_idx:
                return False
        return True

    def check_doesnt_end_in_dot(self):
        for item in self.closure:
            if len(item.rhs) <= item.dot_idx:
                return False
        return True

    def get_all_after_dot(self):
        return [item.rhs[item.dot_idx] for item in self.closure if item.dot_idx < len(item.rhs)]

    def __eq__(self, other):
        if isinstance(other, State):
            return self.items == other.items and self.closure == other.closure and self.action == other.action
        return False

    def __repr__(self):
        return repr(self.closure)