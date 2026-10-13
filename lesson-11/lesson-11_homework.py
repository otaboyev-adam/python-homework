import sqlite3

# Task 1: Roster

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Roster")
cursor.execute("CREATE TABLE Roster (Name TEXT, Species TEXT, Age INTEGER)")

cursor.execute("INSERT INTO Roster VALUES ('Benjamin Sisko', 'Human', 40)")
cursor.execute("INSERT INTO Roster VALUES ('Jadzia Dax', 'Trill', 300)")
cursor.execute("INSERT INTO Roster VALUES ('Kira Nerys', 'Bajoran', 29)")
conn.commit()

cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
conn.commit()

print("Bajoran characters:")
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
for row in cursor.fetchall():
    print(row[0], "-", row[1])

cursor.execute("DELETE FROM Roster WHERE Age > 100")
conn.commit()

cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
cursor.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
cursor.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
cursor.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")
conn.commit()

print("\nAll characters sorted by age:")
cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
for row in cursor.fetchall():
    print(row)

conn.close()


# Task 2: Library

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Books")
cursor.execute("CREATE TABLE Books (Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)")

cursor.execute("INSERT INTO Books VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction')")
cursor.execute("INSERT INTO Books VALUES ('1984', 'George Orwell', 1949, 'Dystopian')")
cursor.execute("INSERT INTO Books VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')")
conn.commit()

cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
conn.commit()

print("\nDystopian books:")
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
for row in cursor.fetchall():
    print(row[0], "by", row[1])

cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
conn.commit()

cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
cursor.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
cursor.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
cursor.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")
conn.commit()

print("\nAll books sorted by year:")
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
for row in cursor.fetchall():
    print(row)

conn.close()
