import hashtable
from FA import FA
from pif import Pif
from scanner import Scanner

if __name__ == "__main__":
    identifiers = hashtable.HashTable()
    constants = hashtable.HashTable()
    pif = Pif()
    scanner = Scanner()
    fa_int = FA("fa_int.in")
    fa_identifier = FA("fa_id.in")
    with open("p3.txt") as f:
        for line_number, line in enumerate(f):
            scanner.scan(line, identifiers, constants, pif, line_number, fa_int, fa_identifier)

    print("Lexically correct!")

    with open("pif.out", "w") as piff:
        piff.write(repr(pif))

    with open("st.out", "w") as st:
        st.write("IDENTIFIERS\n")
        st.write(repr(identifiers))
        st.write("\n\nCONSTANTS\n")
        st.write(repr(constants))
