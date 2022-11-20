


FA represents a finite automata which reads from an input file the set of states, the alphabet, the input state, the output states and the transitions.
The data structure is made up of a list of states, an alphabet list, the input state as string, a list of output states and a map with tuples as keys for the transitions.

It can check if the FA is a DFA, and, given a sequence, check if the sequence is valid.

In order for the scanner to use the FA there is also a method that gets the first valid sequence from a string.



letter = "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"

digit = "0" | "1" | ... | "9"

char = letter | digit | "-" | "+"

state = {char}


states = state {"," state}

alphabet = char {"," char}

transition = state "," char "=" state

transitions = transition {"\n" transition}

inputFile = states "\n" alphabet "\n" state "\n" states "\n" transitions