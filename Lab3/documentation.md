https://github.com/mihaidaniel34/LFTC/Lab3

This scanner uses two hashtables as symbol tables, one for constants and one for identifiers, and a Pif structure, which holds a list of tuples, consisting of an element and its position in the symbol table, represented as a tuple.

eg: ("identifier", (7,0))


def add(elem, pos):

Description: Adds the tuple to the list

Input: element to be added, position tuple


### Scanner

The scanner looks into the program line by line and by splitting the line into substrings, it verifies if it contains a token by verifying each token in a list of tokens,
an identifier using a regular expression `[a-zA-Z]([a-zA-Z]|\d)*`(identifiers cannot start with a number)  or a constant using `(0|[+-]?[1-9]\d*)|\".*\"` (number or string constant held within quotation marks)