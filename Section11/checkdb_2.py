import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Please enter the name: ")

# for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

db.close()
