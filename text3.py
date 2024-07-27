# Prints from every to the end of the statement 
text = "The event had every promise of happiness for her friend"

for word in text.split()[3:]:
    print(word)

# Prints from event until every, it doesn't include the 4th position 
text = "The event had every promise of happiness for her friend"

for word in text.split()[1:4]:
    print(word)

# Prints had, the word in position 2. end keeps the text in the same line.
text = "The event had every promise of happiness for her friend"

for word in text.split()[2]:
    print(word, end="")