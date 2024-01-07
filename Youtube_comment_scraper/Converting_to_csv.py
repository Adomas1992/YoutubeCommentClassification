import csv

input_file_path = 'comments.txt'
output_file_path = 'comments.csv'

with open(input_file_path, "r", encoding="utf-8") as input_file:

    lines = input_file.readlines()

comments = []

for line in lines:

    line = line.strip()
    if "\t" in line:
        comment, comment_id = line.split("\t", 1)
        comments.append((comment, comment_id))
    else:
        print(f"Skipping line with invalid format: {line}")

with open(output_file_path, "w", newline="", encoding="utf-8") as output_file:

    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["Comment", "Comment ID"])
    csv_writer.writerows(comments)

print(f"Conversion complete. Comments save to {output_file_path}")