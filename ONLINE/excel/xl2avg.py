import openpyxl as xl
import sys
from pprint import pprint as pp

print(sys.argv)
filename = sys.argv[1]

grades = {}

wb = xl.load_workbook(filename)

for ws in wb.worksheets:
    for row in ws.rows:
        name = row[0].value    # string
        grade = row[1].value   # string
        grade = int(grade)     # integer from the string

        # grades[name] += grade   wouldn't work, why?

        if name not in grades:
            grades[name] = grade
        else:
            grades[name] += grade

# pp(grades)

for name in grades:     # name is the key to the grades dictionary
    total = grades[name]
    average = total / len(wb.worksheets)
    print(f"{name} has a {average:.2f}")

wb.close()