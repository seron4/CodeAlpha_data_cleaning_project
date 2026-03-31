import re

def validate_data(name, email):
    if not name or not email:
        return False, "Empty fields"

    # Email format check
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        return False, "Invalid email format"

    return True, "Valid"
def is_false_data(name):
    if len(name) < 2:
        return True
    if name.isnumeric():
        return True
    return False
