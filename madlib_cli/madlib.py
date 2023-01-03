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
    file_path = input(" Enter File Path or hit 'Enter' for the default > ")
    if file_path == "":
        file_path = "assets/madlib.txt"
    try:
        script = read_template(file_path)
        empty_string, parts = parse_template(script)
        filled_list = []
        for i in parts:
            user_input = input(f"  Enter {i} > ")
            filled_list.append(user_input)
        result = merge(empty_string, filled_list)
        print(f"\nHere is your Madlib:\n\n" + result)
        with open('assets/result.txt', 'w') as writer:
            writer.write(result)
    except:
        print('An error occurred')


if __name__ == "__main__":
    main()
    