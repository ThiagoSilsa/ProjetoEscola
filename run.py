# importing sqlite3
import sqlite3

# Stabilishing connection with database
# ".connect" is a method inside sqlite3

# var cnct will be used as a cannection variable
cnct = sqlite3.connect('zerotwoschool')

# cursos is better ´cause we can send an receive informations
# cursor will receive info from database

cursor = cnct.cursor()

# Testing:

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS students
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        class TEXT NOT NULL
        )
    """
)
cnct.commit()
cnct.close()
