from FA import FA


def menu(automata):
    while True:
        inp = input(">")
        match inp:
            case "1":
                print(automata.states)
            case "2":
                print(automata.alphabet)
            case "3":
                print(automata.transition)
            case "4":
                print(automata.initial_state)
            case "5":
                print(automata.final_states)
            case "6":
                print(automata)
            case "7":
                print(check_sequence(automata))
            case "0":
                break
            case _:
                print("Invalid action!")


def check_sequence(automata):
    inp = input("Please enter the sequence\n>").strip().replace(" ", "").split(",")
    return automata.check_sequence(inp)


def print_menu():
    print("1. Print the set of states\n"
          "2. Print the alphabet\n"
          "3. Print the transition functions\n"
          "4. Print the initial state\n"
          "5. Print the set of final states\n"
          "6. Print everything\n"
          "7. Check a sequence\n"
          "0. Exit\n\n")


if __name__ == "__main__":
    fa = FA("fa.in")
    print_menu()
    menu(fa)
    print(fa.deterministic())
