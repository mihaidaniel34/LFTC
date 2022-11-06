import re


class Scanner:
    def __init__(self):
        self.tokens = []
        self.read_tokens()

    def check_token(self, line, idx):
        for token in self.tokens:
            if token == '\"':
                continue
            if line[idx:].startswith(token):
                return token
        return None

    def scan(self, line, identifiers, constants, pif, line_number ):
        line = line.strip()
        idx = 0
        while idx < len(line):
            token = self.check_token(line, idx)
            if token is not None:
                idx += len(token)
                if token != ' ' and token != '\n':
                    pif.add(token, (-1, -1))
            else:
                match = re.match(r'[a-zA-Z]([a-zA-Z]|\d)*', line[idx:])
                if match is not None:
                    pif.add("identifier", identifiers.add(match.group()))
                    idx += len(match.group())
                else:
                    match = re.match(r"(0|[+-]?[1-9]\d*)|\".*\"", line[idx:])
                    if match is not None:
                        const = match.group()
                        if not const.startswith('\"'):
                            const = int(const)
                            if idx + len(repr(const)) < len(line):
                                if line[idx + len(repr(const))].isalpha():
                                    raise RuntimeError(f"LEXICAL ERROR AT LINE {line_number+1}")
                        pif.add("constant", constants.add(const))
                        idx += len(repr(const))
                    else:
                        raise RuntimeError(f"LEXICAL ERROR AT LINE {line_number+1}")

    def read_tokens(self):
        with open("token.in") as f:
            for _ in range(41):
                token = f.readline().strip()
                if token == "space":
                    token = " "
                if token == "newline":
                    token = "\n"
                self.tokens.append(token)

