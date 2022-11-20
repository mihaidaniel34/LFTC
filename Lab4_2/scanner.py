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

    def scan(self, line, identifiers, constants, pif, line_number, fa_int, fa_identifier):
        line = line.strip()
        idx = 0
        while idx < len(line):
            if line[idx] == '+' or line[idx] == '-':
                if pif.get_last()[0] == "constant" or pif.get_last()[0] == "identifier":
                    pif.add(line[idx], (-1, -1))
                    idx += 1
            match = fa_int.get_accepted(line[idx:])
            if match != "":
                if idx + len(match) < len(line):
                    if line[idx + len(match)].isalpha() or line[idx + len(match)].isnumeric():
                        raise RuntimeError(f"LEXICAL ERROR AT LINE {line_number + 1}")
                pif.add("constant", constants.add(match))
                idx += len(match)
            else:
                token = self.check_token(line, idx)
                if token is not None:
                    idx += len(token)
                    if token != ' ' and token != '\n':
                        pif.add(token, (-1, -1))
                else:
                    # match = re.match(r'[a-zA-Z]([a-zA-Z]|\d)*', line[idx:])
                    match = fa_identifier.get_accepted(line[idx:])
                    if match != "":
                        pif.add("identifier", identifiers.add(match))
                        idx += len(match)
                    else:
                        match = re.match(r"\".*\"", line[idx:])
                        if match is not None:
                            const = match.group()
                            pif.add("constant", constants.add(const))
                            idx += len(repr(const))
                        else:
                            raise RuntimeError(f"LEXICAL ERROR AT LINE {line_number + 1}")

    def read_tokens(self):
        with open("token.in") as f:
            for _ in range(41):
                token = f.readline().strip()
                if token == "space":
                    token = " "
                if token == "newline":
                    token = "\n"
                self.tokens.append(token)
