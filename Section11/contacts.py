import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 050062113, 'tim@example.com')")
db.execute("INSERT INTO contacts VALUES('Brian',1234,'brian@example.com')")

cursor = db.cursor()
cursor.execute("select * from contacts")

# print(cursor.fetchall())

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name, " ", phone, " ", email)
    print("-" * 35)

cursor.close()
db.commit()
db.close()
