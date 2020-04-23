# 4'ish common text-based data file formats:
#   CSV - Comma Separated Value
#   JSON - JavaScript Object Notation
#   XML - Extensible Markup Language
#   YAML - YAML Ain't Markup Languge

import csv

from pprint import pprint as pp

with open('thousand.csv') as fi:

    # for line in fi:
    #     cells = line.split(',')
    #     cells[2] # could directly access a value in a row

    rdr = csv.reader(fi)

    # for row in rdr:
    #     # each row is a "pre-split" LIST of cells
    #     # pp(row)
    #     # region = row[0].strip()
    #     # date = row[5].strip()
    #     print(f"{row[0].strip():40}{row[5].strip():>10}") # print two of the cells PRETTY
    

    filter_region = 'Europe'
    with open(filter_region + '.csv', 'w', newline='') as out:
        wtr = csv.writer(out) # Be careful to "wrap" the right file

        for row in rdr:
            region = row[0].strip()
            if region == filter_region:
                #print(f"{region:40}{row[5].strip():>10}")
                #wtr.writerow(row)
                ru_row = []
                ru_row.append('Well, duh, It\'s "Europe", yo')
                ru_row.append(row[1])  # country
                ru_row.append(row[2])  # item type
                ru_row.append(row[10]) # price
                wtr.writerow(ru_row)


