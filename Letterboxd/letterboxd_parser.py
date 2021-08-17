'''
Parser for Letterboxd Data
Connor Mentel
Last Mod: 8/12/20
'''

import csv

with open('ratings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    five_star_count = 0
    for row in csv_reader:
        date = row[0]
        name = row[1]
        year = row[2]
        rating = row[4]

        if line_count == 0:
            pass

        else:
            # five star movies
            if float(rating) == 5:
                five_star_count += 1
                print(name)

        line_count += 1

    print("\nYou've logged",five_star_count,"five star movies!\n")