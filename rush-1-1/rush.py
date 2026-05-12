import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = []
        for col in range(x):
            is_top = row == 0
            is_bottom = row == y - 1
            is_left = col == 0
            is_right = col == x - 1

            if (is_top or is_bottom) and (is_left or is_right):
                line.append("o")
            elif is_top or is_bottom:
                line.append("-")
            elif is_left or is_right:
                line.append("|")
            else:
                line.append(" ")
        print("".join(line))