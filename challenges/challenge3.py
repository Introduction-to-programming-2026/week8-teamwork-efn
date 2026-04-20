# challenge3.py — CSV Writer
# Read favorites.csv, count votes per language, write results to language_summary.csv.

import csv

counts = {}

with open("../part1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"]
        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1

total = sum(counts.values())

with open("language_summary.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["language", "votes", "percentage"])
    writer.writeheader()
    for language in sorted(counts, key=counts.get, reverse=True):
        votes = counts[language]
        percentage = round(votes / total * 100, 2)
        writer.writerow({"language": language, "votes": votes, "percentage": percentage})

print("Saved to language_summary.csv")
