phone_book = [("Alice", 4082553555),("", 0000000000), ("Diane", 9830978345), ("Bob", 65038798541), ("", 0000000000), ("Eve", 7642398541), ("Charlie", 5052358753)]
max_size = 19
while len(phone_book) < max_size - 1:
    phone_book.append(("", 0000000000))
    phone_book.append(("Steven", 1420573857))
first_name = input("Lookup which number? ").lower()
first_letter = first_name[0]
first_name = slice(first_name)
search_name = first_name + first_letter
print(first_name)
search_count = 0
for i in range(len(phone_book)):
    search_count += 1
    if search_name == phone_book[i][0]:
        print(phone_book[i][1])
        print(search_count)
        break
    if search_count == max_size:
        print("Name not found")

