import sys
from sys import argv
import csv

print("*** Program do zarządzania plikami csv ***")

input_file, output_file, changes = sys.argv[1], sys.argv[2], sys.argv[3:]
print(input_file, output_file, changes)


# with open("in.csv") as file:
#     zmienna = csv.reader(file)
#     for row in zmienna:
#         inflation_list.append(float(row[0]))

