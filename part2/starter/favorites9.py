# favorites9.py
# Task: Count languages using SQL instead of a Python dictionary.
#
# Before running this file, import the CSV into SQLite:
#   sqlite3 favorites.db
#   .mode csv
#   .import ../week1/favorites.csv favorites
#   .quit
#
# The SQL query replaces the entire counting loop from favorites5–8.
# One query does what 10+ lines of Python did.
#
# Expected output:
#   Python 196
#   C 40
#   Scratch 28

from cs50 import SQL

db = SQL("sqlite:///favorites.db")

rows = db.execute("SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC")

for row in rows:
    print(row["language"], row["n"])
