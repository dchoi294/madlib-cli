import read


def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as f_error:
        raise f_error


def parse_template(string):
    separate = tuple(read.findall(r"{([^{}]*)}", string))
    for i in separate:
        string = string.replace(i, "")
    return string, separate


def merge(bare, input):
    return bare.format(input)


intro = """
**************************************
**       Hello there, Welcome!      **
**                                  **
**************************************
"""


if __name__ == "__main__":
    print(intro)
    file = read_template("assets/madlib.txt")
    string, parts = parse_template(file)
    filled = []
    for i in parts:
        print(i)
        user_input = input("> ")
        filled.append(user_input)
    result = merge(string, filled)
