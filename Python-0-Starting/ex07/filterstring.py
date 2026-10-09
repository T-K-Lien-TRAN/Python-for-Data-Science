import sys


def main():
    """
    Filter words from a string based on their length.
    The program accepts exactly two command-line arguments:
    a string containing words and an integer N.
    It splits the input string into individual words using split().
    A lambda function checks whether each word has more than N
    characters, and filter() selects the words satisfying this condition.
    A list comprehension creates a list of the filtered words.
    The program prints the resulting list to standard output.
    If the number of arguments is incorrect or the second argument
    cannot be converted to an integer, an AssertionError is raised
    and an error message is displayed.
    Examples:
        Input:  python3 filterstring.py "Hello the World" 4
        Output: ['Hello', 'World']

        Input:  python3 filterstring.py "Hello World" 99
        Output: []

        Input:  python3 filterstring.py 3 "Hello the World"
        Output: AssertionError: the arguments are bad
    """

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bed")
        text = sys.argv[1].split()
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bed")
        result = [word for word in filter(lambda w: len(w) > N, text)]
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
