from data_structures_and_algorithms import Record

record = Record()

record.insert('name', "Kevin")
record.insert('age', "41")
record.insert('gender', "Male")

record.print_record()

record.insert('name', "Kevin")
record.insert('age', "41")
record.insert('gender', "Male")

record.delete('age')

record.print_record()

record.insert('name', "Kevin")
record.insert('age', "41")
record.insert('gender', "Male")

record.print_record()

record.search('gender')

record.update('age', '42')

record.print_record()

print(f'record_size is: {record.size()}')

record.clear_record()

record.clear_record()

record.print_record()

record.insert('name', "Kevin")
record.insert('age', "41")
record.insert('gender', "Male")
record.insert('occupation', "SW Test Engineer")

record.print_record()
record.traverse()
