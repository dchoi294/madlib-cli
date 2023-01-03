def read_template(file_name):
    try:
        with open(file_name) as f:
            return f.read()
    except FileNotFoundError as f_error:
        raise f_error


def parse_template(template):
    base = ""
    parts_list = []
    check = False
    part = ""
    for char in template:
        if char == "{":
            base += char
            check = True
        elif char == "}":
            base += char
            parts_list.append(part)
            part = ""
            check = False
        elif check is False:
            base += char
        elif check is True:
            part += char
    return base, tuple(parts_list)


def merge(bare, input):
    return bare.format(*input)


intro = """
**************************************
**       Hello there, Welcome!      **
**                                  **
**************************************
"""


def main():
    print(intro)
    file = read_template("assets/madlib.txt")
    string, parts = parse_template(file)
    filled = []
    for i in parts:
        print(i)
        user_input = input("> ")
        filled.append(user_input)
    result = merge(string, filled)


if __name__ == "__main__":
    main()
    