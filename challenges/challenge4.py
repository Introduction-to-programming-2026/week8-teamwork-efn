# challenge4.py — SQL Explorer
# Present an interactive menu that runs different SQL queries on favorites.db.
# Requires favorites.db — see week2/README.md for setup instructions.

import sqlite3

conn = sqlite3.connect("favorites.db")
db = conn.cursor()

while True:
    print("\n=== SQL Explorer ===")
    print("1. Count by language")
    print("2. Count by problem")
    print("3. Search by problem name")
    print("4. Top 5 problems overall")
    print("5. Quit")
    choice = input("Choice: ")

    if choice == "1":
        rows = db.execute("SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC").fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}")

    elif choice == "2":
        rows = db.execute("SELECT problem, COUNT(*) AS n FROM favorites GROUP BY problem ORDER BY n DESC").fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}")

    elif choice == "3":
        name = input("Problem name: ")
        rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", (name,)).fetchall()
        print(f"{rows[0][0]} students chose {name}")

    elif choice == "4":
        rows = db.execute("SELECT problem, COUNT(*) AS n FROM favorites GROUP BY problem ORDER BY n DESC LIMIT 5").fetchall()
        for i, row in enumerate(rows, start=1):
            print(f"{i}. {row[0]} ({row[1]})")

    elif choice == "5":
        break

conn.close()
