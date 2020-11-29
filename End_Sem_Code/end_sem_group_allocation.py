import pandas as pd
import csv
import re
import os
import shutil


def creating_groups_dir(filename):
    if os.path.isdir(os.path.join(os.getcwd(), 'groups')):
        shutil.rmtree(os.path.join(os.getcwd(), 'groups'))
    os.mkdir('groups')


def branchwise_creator(new_file, rows):
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


def groupwise_creator(new_file, row):
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


def stats_file_creator(new_file, row, fieldnames):
    if os.path.isfile(new_file):
        with open(new_file, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(row)
            file.close()
    else:
        with open(new_file, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(row)
            file.close()


def group_allocation(filename, number_of_groups):
    creating_groups_dir(filename)
    data = pd.read_csv(filename)
    data.set_index('Roll', inplace=True)
    data.sort_values(["Roll"], axis=0, ascending=True, inplace=True)
    file_name_sorted = "sorted_temp_master_data.csv"
    data.to_csv(file_name_sorted)
    df = pd.read_csv(file_name_sorted)
    branch_strength = {}
    branch_names = []
    i = 0
    # creating csv files for individual branches with student ingfo
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
    # print(row)
    branch_strength = {}

    # Creating branch_strength.csv file
    for i in range(len(row)):
        rows = {'BRANCH_CODE': row[i][0], 'STRENGTH': row[i][1]}
        branch_strength[row[i][0]] = row[i][1]
        # print(rows)
        new_file1 = 'branch_strength.csv'
        new_dir = os.path.join(os.getcwd(), 'groups')
        new_file = os.path.join(new_dir, new_file1)
        branchwise_creator(new_file, rows)
    # number_of_groups = input("Kindly enter the number of groups needed for segregation - ")
    k = 0

    # Creating group files for G01 to G12
    gb_strength = {}
    for key, value in branch_strength.items():
        # print(key, value)
        group_strength = []

        groups = []
        for i in range(1, number_of_groups+1):
            group_strength.append(int(value/number_of_groups))
        for i in range(1, value % number_of_groups+1):
            group_strength[(k+i) % number_of_groups-1] += 1
        k = (k+i) % number_of_groups
        # print(group_strength, k)
        gb_strength[key] = group_strength
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
                        groups.append(new_file1)
                    else:
                        new_file1 = 'Group_G' + str(i) + '.csv'
                        groups.append(new_file1)
                    new_dir = os.path.join(os.getcwd(), 'groups')
                    new_file = os.path.join(new_dir, new_file1)
                    groupwise_creator(new_file, row)
                    j += 1
                elif j == group_strength[i-1]:
                    if i < 10:
                        new_file1 = 'Group_G0' + str(i) + '.csv'
                        groups.append(new_file1)
                    else:
                        new_file1 = 'Group_G' + str(i) + '.csv'
                        groups.append(new_file1)
                    new_dir = os.path.join(os.getcwd(), 'groups')
                    new_file = os.path.join(new_dir, new_file1)
                    groupwise_creator(new_file, row)
                    j = 1
                    i += 1

    # Creating stats_grouping.csv file
    for i in range(0, number_of_groups):
        row = {}
        fieldnames = []
        row['Group_number'] = groups[i]
        row['Total'] = 0
        fieldnames.append('Group_number')
        fieldnames.append('Total')
        # print(gb_strength)
        for j in gb_strength.keys():
            # print(j)
            row[j] = gb_strength[j][i]
            row['Total'] += row[j]
            fieldnames.append(j)
        # print(row)
        # return
        new_file1 = 'stats_grouping.csv'
        new_dir = os.path.join(os.getcwd(), 'groups')
        new_file = os.path.join(new_dir, new_file1)
        stats_file_creator(new_file, row, fieldnames)
    os.remove(file_name_sorted)


filename = "Btech_2020_master_data.csv"

number_of_groups = 12
group_allocation(filename, number_of_groups)
