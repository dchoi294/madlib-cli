
def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as f_error:
        raise f_error


def parse_template(string):
    separate = tuple(string)
    for i in separate:
        string = string.replace(i, "")
    return string, separate


def merge(bare, input):
    return bare.format(input)


intro = """
**************************************
**       Hello, there Welcome!      **
**                                  **
**************************************
"""

print(intro)