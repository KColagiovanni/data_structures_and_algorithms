import csv
import random

data = []
dict_data = {}
csv_filename = 'random_record.csv'
number_of_records = 100
min_num = 18
max_num = 120

# Delete file contents
with open(csv_filename, 'r+', newline='') as file:
    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Truncate the file, deleting all its contents
    file.truncate()

for record_id in range(number_of_records):
    new_record = [
        int(record_id),
        f'name_' + str(record_id),
        random.randint(min_num, max_num),
        random.choice(['Male', 'Female'])
    ]

    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        print(f'new_record is: {new_record}')
        writer.writerow(new_record)

print(f"CSV file '{csv_filename}' created successfully.")