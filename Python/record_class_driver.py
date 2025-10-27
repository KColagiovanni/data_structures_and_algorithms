from data_structures_and_algorithms import Record
import csv

csv_filename = 'random_record.csv'

def record_example_test():
    record = Record()
    count = 0

    count += 1
    print(f'\n{count}')  # 1
    record.insert_record(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male'})  # Pass - Record inserted successfully.

    count += 1
    print(f'\n{count}')  # 2
    record.print_record()

    count += 1
    print(f'\n{count}')  # 3
    record.insert_record(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male'})  # Fail - Record already exists.

    count += 1
    print(f'\n{count}')  # 4
    record.delete_record(1)  # Pass - Delete successful.

    count += 1
    print(f'\n{count}')  # 5
    record.delete_record(1)  # Fail - Doesn't exist.

    count += 1
    print(f'\n{count}')  # 6
    record.print_record()

    count += 1
    print(f'\n{count}')  # 7
    record.insert_record(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male'})  # Pass - Record inserted successfully.

    count += 1
    print(f'\n{count}')  # 8
    record.print_record()

    count += 1
    print(f'\n{count}')  # 9
    record.delete_record_value(1, 'gender')

    count += 1
    print(f'\n{count}')  # 10
    record.print_record()

    count += 1
    print(f'\n{count}')  # 11
    record.insert_new_item(1, 'gender', 'Male')  # Pass - Update successful.

    count += 1
    print(f'\n{count}')  # 12
    record.print_record()

    count += 1
    print(f'\n{count}')  # 13
    record.search(1)  # Pass - Record value found.

    count += 1
    print(f'\n{count}')  # 14
    record.update(1, 'age', '42')  # Pass - Update successful.

    count += 1
    print(f'\n{count}')  # 15
    record.print_record()

    count += 1
    print(f'\n{count}')  # 16
    print(f'record_size is: {record.size()}')  # Record size 1

    count += 1
    print(f'\n{count}')  # 17
    record.delete_all()  # Pass - Delete all successful

    count += 1
    print(f'\n{count}')  # 18
    record.delete_all()  # Fail - No records exist

    count += 1
    print(f'\n{count}')  # 19
    record.print_record()

    count += 1
    print(f'\n{count}')  # 20
    record.insert_record(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male', 'occupation': 'SW Test Engineer'})  # Record #1

    count += 1
    print(f'\n{count}')  # 21
    record.insert_record(2, {'name': 'Andrew', 'age': '4', 'gender': 'Male'})  # Record #2

    count += 1
    print(f'\n{count}')  # 22
    print(f'record_size is: {record.size()}')  # Record size 2

    count += 1
    print(f'\n{count}')  # 23
    record.print_record()

    count += 1
    print(f'\n{count}')  # 24
    record.traverse()

def read_from_csv():

    record = Record()

    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            record.insert_record(
                row[0],
                {
                    'name':row[1],
                    'age':row[2],
                    'gender':row[3]
                }
            )
    record.traverse()

# record_example_test()
read_from_csv()
