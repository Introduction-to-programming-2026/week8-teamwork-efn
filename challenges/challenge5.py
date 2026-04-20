# challenge5.py — Data Cleaner
# Read a messy CSV, detect problems, write a cleaned version, print a report.
# Create your own messy_data.csv with intentional errors to test against.

import csv

valid_languages = {"Python", "C", "Scratch"}
seen_ids = set()

removed_blank = 0
removed_duplicate = 0
removed_invalid_score = 0
removed_unknown_language = 0
fixed_missing_score = 0

cleaned_rows = []

with open("messy_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_id = row["student_id"].strip()
        language = row["language"].strip()
        score_raw = row["score"].strip()

        if not student_id or not language:
            removed_blank += 1
            continue

        if student_id in seen_ids:
            removed_duplicate += 1
            continue

        if language not in valid_languages:
            removed_unknown_language += 1
            continue

        if not score_raw:
            fixed_missing_score += 1
            score = ""
        else:
            score = int(score_raw)
            if score < 1 or score > 5:
                removed_invalid_score += 1
                continue

        seen_ids.add(student_id)
        cleaned_rows.append({"student_id": student_id, "language": language, "score": score})

with open("cleaned_data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["student_id", "language", "score"])
    writer.writeheader()
    writer.writerows(cleaned_rows)

print("=== Cleaning Report ===")
print(f"Rows kept        : {len(cleaned_rows)}")
print(f"Blank rows       : {removed_blank}")
print(f"Duplicates       : {removed_duplicate}")
print(f"Invalid scores   : {removed_invalid_score}")
print(f"Unknown languages: {removed_unknown_language}")
print(f"Missing scores   : {fixed_missing_score}")
print("Saved to cleaned_data.csv")
