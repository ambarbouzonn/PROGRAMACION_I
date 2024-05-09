def validate_number(number:int|float, minimum:int|float, maximum:int|float) -> bool:
    if number >= minimum and number <= maximum:
        return True
    else:
        return False

def validate_length(string:str, length:int) -> bool:
    if len(string) == length:
            return True
    else:
        return False