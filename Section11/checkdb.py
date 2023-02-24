import sqlite3

db = sqlite3.connect("contacts.sqlite")

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name, " ", phone, " ", email)
    print("-" * 35)

# for row in db.execute("SELECT * FROM sqlite_master"):
#     print(row)
#     print("-" * 35)

db.close()
