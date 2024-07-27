# x = input("x: ")
# y = input("y: ")

# # print(int(x) + int(y))

# print(int(x)/int(y))

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not an integer")
            # pass (Asks u again if u don't enter an integer)

def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print(x+y)

main()