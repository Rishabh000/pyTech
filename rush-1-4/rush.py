import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if x == 1 or y == 1:
        for _ in range(y):
            print("B" * x)
        return

    for row in range(y):
        line = []
        for col in range(x):
            is_top = row == 0
            is_bottom = row == y - 1
            is_left = col == 0
            is_right = col == x - 1

            if (is_top or is_bottom) and is_left:
                line.append("A")
            elif (is_top or is_bottom) and is_right:
                line.append("C")
            elif is_top or is_bottom or is_left or is_right:
                line.append("B")
            else:
                line.append(" ")
        print("".join(line))
