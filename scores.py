def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not an integer")
            # pass (Asks u again if u don't enter an integer)
scores = []
for i in range(3):
    score = get_int("Score: ")
    #scores.append(score)
    # append: add the score to the score array
    scores = scores + [score]

average = sum(scores) / len(scores)
print(f"Average: {average}")
