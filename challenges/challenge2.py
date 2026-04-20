# challenge2.py — Two-Column Report
# Read favorites.csv, find the most common problem per language, print a table.

import csv

problems = {}

with open("../part1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"]
        problem = row["problem"]
        if language not in problems:
            problems[language] = {}
        if problem in problems[language]:
            problems[language][problem] += 1
        else:
            problems[language][problem] = 1

print(f"{'Language':<10} | Most Common Problem")
print("-" * 11 + "+" + "-" * 20)

for language in sorted(problems):
    top_problem = max(problems[language], key=problems[language].get)
    print(f"{language:<10} | {top_problem}")
