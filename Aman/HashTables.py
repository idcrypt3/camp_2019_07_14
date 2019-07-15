# Lesson for creating a database with hash functions for efficient lookup functions
# Hash tables used in some cryptanalytic functions to cut down solve times

# Hash function
def new_hash(message):
    digest = 0
    if message == "":
        digest = -1
    for c in message:
        digest += ord(c)
    digest = digest % max_size
    return digest


# Unsorted phonebook
phone_book = [
    ("Alice", 4082553555),
    ("", 0000000000),
    ("Diane", 9830978345),
    ("Bob", 6503879023),
    ("", 0000000000),
    ("Eve", 7642398541),
    ("Charlie", 5052358753)
]
max_size = 19
while len(phone_book) < max_size - 1:
    phone_book.append(("", 0000000000))
phone_book.append(("Steven", 1420573857))

# Alphabetical sort
sorted_book = sorted(phone_book, key=lambda phone_book: phone_book[0])
# Truncate all empty entries from this book
while sorted_book[0][0] == "":
    del (sorted_book[0])

# Hashed sort
phone_hash = []
hashed_book = [("", 0000000000) for _ in range(max_size)]
for i in range(len(phone_book)):
    name = phone_book[i][0]
    digest = new_hash(name)
    if digest == -1:
        continue
    phone_hash.append(digest)
    new_index = digest
    while hashed_book[new_index] != ("", 0000000000):
        # Some hash tables use a second hash function or even a list of lists (of tuples)!
        new_index = (new_index + 1) % max_size
    hashed_book[new_index] = phone_book[i]
# Compare hashed_book placement with indexes in phone_hash
# print(hashed_book)
# print(phone_hash)

# Find the phone number of the inputted name and compare search times (operations in this case)
search_name = input("Lookup which number?")
search_count = 0
# Search original phonebook by iterating from index 0 to size - 1 (and takes up to size steps)
# The built-in list.index() and list.count() methods follow this same format!
for i in range(len(phone_book)):
    search_count += 1
    if phone_book[i][0] == search_name:
        print("Unsorted book search:")
        print(phone_book[i][1])
        print(search_count)
        break
    if search_count == max_size:
        print("Not found (unsorted)")

# Search alphabetical phonebook by starting halfway through and checking relatively alphabet order
# This search takes up to a number of steps based on the log of the list's size: ln(len(list))
search_index = int(len(sorted_book) / 2)
search_max = len(sorted_book) - 1
search_min = 0
search_count = 0
for i in range(len(sorted_book)):
    search_count += 1
    if search_name == sorted_book[search_index][0]:
        print("Sorted book search:")
        print(sorted_book[search_index][1])
        print(search_count)
        break
    elif search_name < sorted_book[search_index][0]:
        search_max = search_index
        search_index -= int((search_index - search_min) / 2 + 0.5)
    elif search_name > sorted_book[search_index][0]:
        search_min = search_index
        search_index += int((search_max - search_index) / 2 + 0.5)
    if search_count == len(sorted_book):
        print("Not found (alphabetical)")

# Search hashed phonebook by using the hash of the input
# This search will typically be 3 steps at most based on hash function design and list size!
hash_index = new_hash(search_name)
for i in range(len(hashed_book)):
    search_count += 1
search_count = 0
    if hashed_book[hash_index][0] == search_name:
        print("Hashed book search:")
        print(hashed_book[hash_index][1])
        print(search_count)
        break
    hash_index = (hash_index + 1) % max_size
    if search_count == max_size:
        print("Not found (hashed)")