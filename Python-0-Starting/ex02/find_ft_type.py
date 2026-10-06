from typing import Any
def all_thing_is_obj(object: Any) -> int:
    ob_type = type(object)
    if ob_type is list:
        print(f"List : {ob_type}")
    elif ob_type is tuple:
        print(f"Tuple : {ob_type}")
    elif ob_type is set:
        print(f"Set : {ob_type}")
    elif ob_type is dict:
        print(f"Dict : {ob_type}")
    elif ob_type is str:
        print(f"{object} is in the kitchen : {ob_type}")
    else:
        print("Type not found")
    return 42