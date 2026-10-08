import sys


def main():
    """
    Convert a command-line string into Morse code.

    The program accepts exactly one argument containing letters (A-Z,
    a-z), digits (0-9), and spaces. It converts the input to uppercase
    and validates each character against the Morse code dictionary.

    Each valid character is translated into its Morse representation.
    Morse codes are separated by spaces, and spaces in the original
    text are represented by '/'.

    If the number of arguments is incorrect or an invalid character
    is found, the program raises an AssertionError and displays
    an error message.

    The final Morse code translation is printed to standard output.

    Example:
        Input:  python3 sos.py "sos"
        Output: ... --- ...
    """
    try:
        NESTED_MORSE = {
                        " ": "/",
                        "A": ".-",
                        "B": "-...",
                        "C": "-.-.",
                        "D": "-..",
                        "E": ".",
                        "F": "..-.",
                        "G": "--.",
                        "H": "....",
                        "I": "..",
                        "J": ".---",
                        "K": "-.-",
                        "L": ".-..",
                        "M": "--",
                        "N": "-.",
                        "O": "---",
                        "P": ".--.",
                        "Q": "--.-",
                        "R": ".-.",
                        "S": "...",
                        "T": "-",
                        "U": "..-",
                        "V": "...-",
                        "W": ".--",
                        "X": "-..-",
                        "Y": "-.--",
                        "Z": "--..",
                        "0": "-----",
                        "1": ".----",
                        "2": "..---",
                        "3": "...--",
                        "4": "....-",
                        "5": ".....",
                        "6": "-....",
                        "7": "--...",
                        "8": "---..",
                        "9": "----."
                    }
        if (len(sys.argv) != 2 or
                not all(c in NESTED_MORSE for c in sys.argv[1].upper())):
            raise AssertionError("the arguments are bed")
        text = sys.argv[1].upper()
        result = " ".join(NESTED_MORSE[c] for c in text)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
