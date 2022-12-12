# lr(0)
from LR import LR
from grammar import Grammar
from item import Item


def menu(gr):
    while True:
        inp = input(">")
        match inp:
            case "1":
                print(gr.non_terminals)
            case "2":
                print(gr.terminals)
            case "3":
                print(gr.starting_nt)
            case "4":
                print(gr.productions)
            case "5":
                print(gr.cfg_check())
            case "0":
                break
            case _:
                print("Invalid action!")


def print_menu():
    print("1. Print the set of non-terminals\n"
          "2. Print the set of terminals\n"
          "3. Print the starting non-terminal\n"
          "4. Print the productions\n"
          "5. Check if the grammar is context free\n"
          "0. Exit\n\n")


if __name__ == "__main__":
    grammar = Grammar("g1.txt")
    print_menu()
    menu(grammar)
    print(grammar.cfg_check())

    lr = LR(grammar)
    start_item = Item(grammar.starting_nt, grammar.get_prod(grammar.starting_nt), 0)
    print(lr.closure(start_item))