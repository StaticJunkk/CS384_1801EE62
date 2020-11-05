import csv
import os
import re
import shutil
import pandas as pd

direct_path = os.path.join(os.getcwd(), 'grades')


def del_create_grades_folder():
    if os.path.isdir(direct_path):
        shutil.rmtree(direct_path)
    # creating fresh empty grades folder
    os.mkdir(direct_path)


def roll_number_individual():
    try:
        with open('acad_res_stud_grades.csv') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                roll_no = row['roll']
                folder_path = os.path.join(
                    os.getcwd(), 'grades')
                file_name = roll_no + '_individual.csv'
                file_path = os.path.join(folder_path, file_name)
                data_entry = {'Subject': row['sub_code'], 'Credits': row['total_credits'],
                              'Type': row['sub_type'], 'Grade': row['credit_obtained'], 'Sem': row['sem']}
                if os.path.isfile(file_path):
                    # opening file in append mode, then writing the current row, with header
                    try:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'Subject', 'Credits', 'Type', 'Grade', 'Sem'])
                            writer.writerow(data_entry)
                            file.close()
                    except:
                        print(f"Error opening {file_name}")
                else:
                    try:
                        with open(file_path, 'a+', newline='') as file:
                            file.write(f'Roll: {roll_no}\n')
                            file.write('Semester Wise Details\n')
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'Subject', 'Credits', 'Type', 'Grade', 'Sem'])
                            writer.writeheader()
                            writer.writerow(data_entry)
                            file.close()
                    except:
                        print(f"Error opening {file_name}")

    except:
        print("Error while opening acad_res_stud_grades.csv")

    # except:
    #     print("Error while opening acad_res_stud_grades.csv")


def roll_number_overall():
    os.chdir(direct_path)
    for file in os.listdir(direct_path):
        name_file = re.split('_', str(file), maxsplit=1)
        roll_no = name_file[0]
        if(name_file[1] == 'overall.csv'):
            continue
        else:
            df = pd.read_csv(file, skiprows=2)
            data = dict(df)
            creds = list(data['Grade'])
            i = 0
            for grade in creds:
                if grade == 'AA':
                    creds[i] = 10
                elif grade == 'AB':
                    creds[i] = 9
                elif grade == 'BB':
                    creds[i] = 8
                elif grade == 'BC':
                    creds[i] = 7
                elif grade == 'CC':
                    creds[i] = 6
                elif grade == 'CD':
                    creds[i] = 5
                elif grade == 'DD':
                    creds[i] = 4
                elif grade == 'F' or grade == 'I':
                    creds[i] = 0
                i += 1
            sem = set(df['Sem'])
            keys = list(sem)
            sem = {}
            semwise_score = {}
            semwise_credits = {}
            total_credits = {}
            SPI = {}
            CPI = {}
            for key in keys:
                try:
                    sem[key] = key
                    semwise_score[key] = 0
                    semwise_credits[key] = 0
                    SPI[key] = 0
                    CPI[key] = 0
                    total_credits[key] = 0
                except:
                    pass
            i = 0
            for value in df['Sem']:
                try:
                    semwise_score[value] += creds[i]*df['Credits'][i]
                    semwise_credits[value] += df['Credits'][i]
                except:
                    pass
                i += 1
            for key in keys:
                try:
                    SPI[key] = round(semwise_score[key] /
                                     semwise_credits[key], 2)
                    CPI[key] = SPI[key]
                except:
                    pass
            i = 0
            for key in keys:
                try:
                    if i == 0:
                        total_credits[key] = semwise_credits[key]
                    else:
                        total_credits[key] += (semwise_credits[key] + x)
                    x = total_credits[key]
                except:
                    pass
                i += 1
            i = 0
            for key in keys:
                try:
                    x = 0
                    for j in range(1, i+2):
                        #print(key, SPI[j], semwise_credits[j])
                        x += SPI[j]*semwise_credits[j]
                    CPI[key] = round(x/total_credits[key], 2)
                    i += 1
                    if(i > int(key)):
                        break
                except:
                    pass
            data_entry = []
            for key in keys:
                lst = [sem[key], semwise_credits[key], semwise_credits[key],
                       SPI[key], total_credits[key], total_credits[key], CPI[key]]
                data_entry.append(lst)
            folder_path = direct_path
            file_name = roll_no + '_overall.csv'
            file_path = os.path.join(folder_path, file_name)
            for row in data_entry:
                if os.path.isfile(file_path):
                    # opening file in append mode, then writing the current row, with header
                    try:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(row)
                            file.close()
                    except:
                        print(f"Error opening {file_name}")
                else:
                    try:
                        with open(file_path, 'a+', newline='') as file:
                            file.write(f'Roll: {roll_no}\n')
                            writer = csv.writer(file)
                            fieldnames = ['Semester', 'Semester Credits', 'Semester Credits Cleared',
                                          'SPI', 'Total Credits', 'Total Credits Cleared', 'CPI']
                            writer.writerow(fieldnames)
                            writer.writerow(row)
                            file.close()
                    except:
                        print(f"Error opening {file_name}")
        break


# del_create_grades_folder()
# roll_number_individual()
roll_number_overall()
