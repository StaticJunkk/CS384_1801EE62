import pandas as pd
import csv
import re
import os


def group_allocation(filename, number_of_groups):
    df = pd.read_csv(filename)
    total_students = len(df)
    branch_strength = {}
    branch_names = []
    i = 0
    for data in df['Roll']:
        branch = re.split('\d+', str(data))[1]
        filename = branch.upper() + '.csv'
        row = {'Roll': df['Roll'][i], 'Name': df['Name']
               [i], 'Email': df['Email'][i]}
        if os.path.isfile(filename):
            with open(filename, 'a+', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['Roll', 'Name', 'Email'])
                writer.writerow(row)
        else:
            with open(filename, 'a+', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['Roll', 'Name', 'Email'])
                writer.writeheader()
                writer.writerow(row)
        if branch in branch_names:
            pass
        else:
            branch_names.append(branch)
            branch_strength[branch] = 0
        branch_strength[branch] += 1
        i += 1
    row = sorted(branch_strength.items(), key=lambda x: x[1])
    print(row)
    for i in range(len(row)):
        rows = {'BRANCH_CODE': row[i][0], 'STRENGTH': row[i][1]}
        print(rows)
        if os.path.isfile('branch_strength.csv'):
            with open('branch_strength.csv', 'a+', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['BRANCH_CODE', 'STRENGTH'])
                writer.writerow(rows)
                file.close()
        else:
            with open('branch_strength.csv', 'a+', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['BRANCH_CODE', 'STRENGTH'])
                writer.writeheader()
                writer.writerow(rows)
                file.close()


filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)
