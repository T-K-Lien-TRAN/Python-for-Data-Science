def count_in_list(lst: list, item: object) -> int:
    """Count how many times an item appears in a list."""

    count = 0
    for element in lst:
        if element == item:
            count += 1
    return count
