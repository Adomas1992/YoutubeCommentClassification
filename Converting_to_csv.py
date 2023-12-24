import csv
import os
import re

# Method to remove emojis (optional, if desired)
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)

# Get the input file's name and path
input_file_path = "comments.txt"  # Replace with your TXT file path
output_filename = os.path.splitext(input_file_path)[0] + ".csv"

try:
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)

        for line in infile:
            line = line.strip()
            if line and not bool(re.match('^\s*$', line)) and not bool(re.match('^[' + emoji_pattern.pattern + ']+$', line)):
                try:
                    comment, comment_id = line.rsplit(maxsplit=1, sep='\t')  # Split by tab
                    # ... rest of your code
                except ValueError:
                    print("Skipping line with invalid format:", line)

except (UnicodeDecodeError, ValueError) as e:
    print("Error:", e)
