
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
**         The year is 1965.        **
**                                  **
**  You're bored out of your mind.  **
**                                  **
**   I know! Let's put words into   **
**   a partially-completed story.   **
**                                  **
**      What a terrible time to     **
**             be alive.            **
**                                  **
**     Enter a lower-cased word     **
**    or number for each prompt.    **
**************************************
"""

print(intro)