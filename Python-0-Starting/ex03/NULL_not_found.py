from typing import Any

def NULL_not_found(object: Any) -> int:
    ob_type = type(object)
    if object is None:
        print(f"Nothing: {object} {ob_type}")
    elif ob_type is float and object != object:
        print(f"Cheese: {object} {ob_type}")
    elif ob_type is int and object == 0:
        print(f"Zero: {object} {ob_type}")
    elif ob_type is str and object == "":
        print(f"Empty: {ob_type}")
    elif ob_type is bool and object is False:
        print(f"Fake: {object} {ob_type}")    
    else:
        print("Type not Found")
        return 1
    return 0