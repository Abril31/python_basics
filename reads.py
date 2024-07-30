import csv

books = []

# Add book by reading from books.csv. Create a list of dictionaries
# Use a loop to creat a dict for each row.
with open("books.csv") as file:
   reader = csv.DictReader(file) 
   for row in reader:
      books.append(row)

for book in books:
    print(book)