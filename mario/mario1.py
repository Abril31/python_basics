
while True:
    try:
        h = int(input("Height: "))
        if h > 0 and h < 9:
            break
        else:
            print("Enter a height between 1 and 8.")
    except ValueError:
        print("Invalid input. Enter a valid integer.")

def main():
    for m in range(h):
        print(blanks(h - m) + hashes(m + 1))


def blanks(h):
    return (" " * (h-1))


def hashes(h):
    return ("#"*h)


main()
