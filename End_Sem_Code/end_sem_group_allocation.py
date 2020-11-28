import pandas as pd
import csv
import re
import os
import shutil


def group_allocation(filename, number_of_groups):
    if os.path.isdir(os.path.join(os.getcwd(), 'groups')):
        shutil.rmtree(os.path.join(os.getcwd(), 'groups'))
    os.mkdir('groups')
    df = pd.read_csv(filename)
    total_students = len(df)
    branch_strength = {}
    branch_names = []
    i = 0
    for data in df['Roll']:
        branch = re.split('\d+', str(data))[1]
        filename1 = branch.upper() + '.csv'
        row = {'Roll': df['Roll'][i], 'Name': df['Name']
               [i], 'Email': df['Email'][i]}
        new_dir = os.path.join(os.getcwd(), 'groups')
        new_file = os.path.join(new_dir, filename1)
        if os.path.isfile(new_file):
            with open(new_file, 'a+', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['Roll', 'Name', 'Email'])
                writer.writerow(row)
        else:
            with open(new_file, 'a+', newline='') as file:
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
    row = sorted(branch_strength.items(), key=lambda x: x[1], reverse=True)
    print(row)
    for i in range(len(row)):
        rows = {'BRANCH_CODE': row[i][0], 'STRENGTH': row[i][1]}
        print(rows)
        new_file1 = 'branch_strength.csv'
        new_dir = os.path.join(os.getcwd(), 'groups')
        new_file = os.path.join(new_dir, new_file1)
        if os.path.isfile(new_file):
            with open(new_file, 'a+', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['BRANCH_CODE', 'STRENGTH'])
                writer.writerow(rows)
                file.close()
        else:
            with open(new_file, 'a+', newline='') as file:
                writer = csv.DictWriter(
                    file, fieldnames=['BRANCH_CODE', 'STRENGTH'])
                writer.writeheader()
                writer.writerow(rows)
                file.close()
    # number_of_groups = input("Kindly enter the number of groups needed for segregation - ")
    for key, value in branch_strength.items():
        # print(key, value)
        group_strength = []
        for i in range(1, number_of_groups+1):
            group_strength.append(int(value/number_of_groups))
        for i in range(1, value % number_of_groups+1):
            group_strength[i-1] += 1
        print(group_strength)
        filename_branch1 = key+'.csv'
        new_dir = os.path.join(os.getcwd(), 'groups')
        filename_branch = os.path.join(new_dir, filename_branch1)
        # print(filename)
        with open(filename_branch) as file:
            i = 1
            j = 1
            reader = csv.DictReader(file)
            for row in reader:
                if j < group_strength[i-1]:
                    if i < 10:
                        new_file1 = 'Group_G0' + str(i) + '.csv'
                    else:
                        new_file1 = 'Group_G' + str(i) + '.csv'
                    new_dir = os.path.join(os.getcwd(), 'groups')
                    new_file = os.path.join(new_dir, new_file1)
                    if os.path.isfile(new_file):
                        with open(new_file, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'Roll', 'Name', 'Email'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(new_file, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'Roll', 'Name', 'Email'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()
                    j += 1
                elif j == group_strength[i-1]:
                    if i < 10:
                        new_file1 = 'Group_G0' + str(i) + '.csv'
                    else:
                        new_file1 = 'Group_G' + str(i) + '.csv'
                    new_dir = os.path.join(os.getcwd(), 'groups')
                    new_file = os.path.join(new_dir, new_file1)
                    if os.path.isfile(new_file):
                        with open(new_file, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'Roll', 'Name', 'Email'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(new_file, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'Roll', 'Name', 'Email'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()
                    j = 1
                    i += 1


filename = "Btech_2020_master_data.csv"

number_of_groups = 12
group_allocation(filename, number_of_groups)
