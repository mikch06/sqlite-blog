class Entry():
    day = 0
    month = 1
    year = 2

entry1 = Entry()
entry2 = Entry()

entry1.goday = 1000
print(f"Test: {entry1.goday}")

entry2.goday = 1002
print(f"Test: {entry1.goday}")
