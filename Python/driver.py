from data_structures_and_algorithms import Record

def record_example_test():
    record = Record()

    record.insert(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male'})  # Pass - Record inserted successfully.

    record.print_record()

    record.insert(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male'})  # Fail - Record already exists.

    record.delete_record(1)  # Pass -Delete successful.

    record.delete_record(1)  # Fail - Doesn't exist.

    record.print_record()

    record.insert(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male'})  # Pass - Record inserted successfully.

    record.print_record()

    record.search('gender')  # Pass - Record value found.

    record.update('age', '42')  # Pass - Update successful.

    record.print_record()

    print(f'record_size is: {record.size()}')  # Record size

    record.delete_all()  # Pass - Clear successful

    record.delete_all()  # Fail - Record doesn't exist

    record.print_record()

    record.insert(1, {'name': 'Kevin', 'age': '41', 'gender': 'Male', 'occupation': 'SW Test Engineer'})
    record.insert(2, {'name': 'Andrew', 'age': '4', 'gender': 'Male'})

    record.print_record()

    record.traverse()


record_example_test()