# starter.py — Language Poll Analyser
# Project 1 | Easy | 20–25 minutes
#
# Run from this folder:
#   python starter.py
#
# The CSV file is at: ../../week1/favorites.csv

import csv

counts = {}

with open("../../part1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"]
        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1

sorted_languages = sorted(counts, key=counts.get, reverse=True)

print("=== Language Popularity Report ===")

for rank, language in enumerate(sorted_languages, start=1):
    print(f"{rank}. {language:<8}: {counts[language]} students")

print(f"\nTotal responses: {sum(counts.values())}")
