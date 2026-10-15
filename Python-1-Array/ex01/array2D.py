def slice_me(family: list, start: int, end: int) -> list:
    """Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end
    arguments
    """
    if not isinstance(family, list) or not family:
        raise TypeError("Family must be a non-empty list")
    if type(start) is not int and type(end) is not int:
        raise TypeError("Start and end must be intergers")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each row must be a list")
    columns = len(family[0])
    rows = len(family)
    if not all(len(row) == columns for row in family):
        raise ValueError("All rows must have the same length")
    print("My shape is:", (rows, columns))
    new_family = family[start:end]
    print("My new shape is:", (len(new_family), columns))
    return new_family


def main():
    """Provide an entry point; tests are in tester.py."""
    pass


if __name__ == "__main__":
    main()
