from sys import argv
import csv

print("\n*** Program do zarządzania plikami csv ***\n")

# Przykładowe wartości
input_file, output_file, changes_list = "in.csv", "out.csv", ["0,0,gitara", "3,1,kubek", "1,2,17", "3,3,0"]

# input_file, output_file, changes_list = sys.argv[1], sys.argv[2], sys.argv[3:]
print(input_file, output_file, changes_list)

rows_list_from_csv = []
changes_list_mod = []

for change in changes_list:
    changes_list_mod.append(change.split(","))

with open(input_file) as file:
    object_csv_file = csv.reader(file)
    for row in object_csv_file:
        rows_list_from_csv.append(row)

print(rows_list_from_csv)

for changes in changes_list_mod:
    row, column, name = changes
    row = int(row)
    column = int(column)
    print(row, column, name)
    rows_list_from_csv[column][row] = name

print(rows_list_from_csv)

with open(output_file, "w", newline="") as file:
    # file.write(rows_list_from_csv)
    write = csv.writer(file, delimiter=",")  # Utworzenie obiektu pliku csv
    for row in rows_list_from_csv:
        write.writerow(row)
