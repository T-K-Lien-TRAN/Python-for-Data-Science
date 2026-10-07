import string
import sys

def main():
    """Read a string and display its length and character counts.
    Accept one command-line argument, or prompt for input if it is missing
    or empty. Count uppercase letters, lowercase letters, punctuation,
    whitespace, and digits. A newline read from stdin counts as whitespace.
    Print an AssertionError message if more than one argument is provided.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1 or sys.argv[1] == "":
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:            
            text = str(sys.argv[1])
        uppercase = 0
        lowercase = 0
        punctuation = 0
        space = 0
        digit = 0
        for character in text:
            if character.isupper():
                uppercase += 1
            elif character.islower():
                lowercase += 1
            elif character in string.punctuation:
                punctuation += 1
            elif character.isspace():
                space += 1
            elif character.isdigit():
                digit += 1    
        print(f"The text contains {len(text)} characters")
        print(f"{uppercase} upper letters")
        print(f"{lowercase} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
if __name__ == "__main__":
    main()
