class ParserOutputNode:
    def __init__(self, index, symbol, parent, sibling):
        self.index = index
        self.symbol = symbol
        self.parent = parent
        self.sibling = sibling

    def __repr__(self):
        return f"Node[{self.index}, {self.symbol}, {self.parent}, {self.sibling}]"


class ParserOutput:
    def __init__(self, output_band, grammar):
        self.output_band = output_band
        self.parsing_tree = []
        self.grammar = grammar

    def has_children(self, node):
        return any(item.parent == node for item in self.parsing_tree)

    def compute_tree(self):
        index = 0
        self.parsing_tree.append(ParserOutputNode(index, self.grammar.initial_snt, -1, -1))
        for prod_id in self.output_band:
            prod = self.grammar.get_prod_by_id(prod_id)
            for node in self.parsing_tree:
                if node.symbol == prod[0][0] and not self.has_children(node.index):
                    parent = node.index
                    index += 1
                    self.parsing_tree.append(ParserOutputNode(index, prod[1][0], parent, -1))
                    for idx in range(1, len(prod[1])):
                        index += 1
                        self.parsing_tree[index - 1].sibling = index
                        self.parsing_tree.append(ParserOutputNode(index, prod[1][idx], parent, -1))
                    break

    def write(self, filename):
        f = open(filename, "w")
        for item in self.parsing_tree:
            f.write(item + "\n")
        f.close()
