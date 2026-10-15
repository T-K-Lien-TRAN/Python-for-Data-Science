def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Return the BMI for each corresponding height and weight."""

    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("Height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("Weight and height must have the same length")
    for w, h in zip(weight, height):
        if type(w) not in (float, int) or type(h) not in (float, int):
            raise TypeError("w, h must be float or integers")
        if w <= 0:
            raise ValueError("Weight must be higher than zero")
        if h <= 0:
            raise ValueError("Height must be higher than zero")
    return [w / h ** 2 for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return whether each BMI is strictly above the limit."""

    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    if type(limit) is not int:
        raise TypeError("limit must be an integer")
    for value in bmi:
        if type(value) not in (int, float):
            raise TypeError("bmi must contain integers or floats.")
    return [value > limit for value in bmi]


def main():
    """Provide an entry point; tests are in tester.py."""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
