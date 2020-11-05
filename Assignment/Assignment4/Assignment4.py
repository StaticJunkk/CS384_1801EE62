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
        grades = ['AA', 'AB', 'BB', 'BC', 'CC', 'CD', 'DD', 'F', 'I']
        with open('acad_res_stud_grades.csv') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                roll_no = row['roll']
                folder_path = os.path.join(
                    os.getcwd(), 'grades')
                file_name = roll_no + '_individual.csv'
                misc_file_name = 'misc.csv'
                file_path = os.path.join(folder_path, file_name)
                data_entry = {'Subject': row['sub_code'], 'Credits': row['total_credits'],
                              'Type': row['sub_type'], 'Grade': row['credit_obtained'], 'Sem': row['sem']}
                if data_entry['Grade'] in grades:
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
                else:
                    print(str(file))
                    fieldname = ['sl', 'roll', 'sem', 'year', 'sub_code',
                                 'total_credits', 'credit_obtained', 'timestamp', 'sub_type']
                    file_path = os.path.join(folder_path, misc_file_name)
                    if os.path.isfile(file_path):
                        # opening file in append mode, then writing the current row, with header
                        try:
                            with open(file_path, 'a+', newline='') as file:
                                writer = csv.DictWriter(
                                    file, fieldnames=fieldname)
                                writer.writerow(row)
                                file.close()
                        except:
                            print(f"Error opening {file_name}")
                    else:
                        try:
                            with open(file_path, 'a+', newline='') as file:
                                writer = csv.DictWriter(
                                    file, fieldnames=fieldname)
                                writer.writeheader()
                                writer.writerow(row)
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
        if str(file) != 'misc.csv':
            name_file = re.split('_', str(file), maxsplit=1)
            roll_no = name_file[0]
            if(name_file[1] == 'overall.csv'):
                continue
            else:
                df = pd.read_csv(file, skiprows=2)
                data = dict(df)
                creds = list(data['Grade'])
                i = 0
                back_log = []
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
                    elif grade == 'F':
                        creds[i] = 0
                        back_log.append(i-1)
                    elif grade == 'I':
                        creds[i] = 0
                    i += 1

                sem = set(df['Sem'])
                keys = list(sem)
                sem = {}
                semwise_score = {}
                semwise_credits = {}
                semwise_credits_cleared = {}
                total_credits = {}
                total_credits_cleared = {}
                SPI = {}
                CPI = {}
                for key in keys:
                    try:
                        sem[key] = key
                        semwise_score[key] = 0
                        semwise_credits[key] = 0
                        semwise_credits_cleared[key] = 0
                        SPI[key] = 0
                        CPI[key] = 0
                        total_credits[key] = 0
                        total_credits_cleared[key] = 0
                    except:
                        pass
                i = 0
                for value in df['Sem']:
                    try:
                        semwise_score[value] += creds[i]*df['Credits'][i]
                        if df['Grade'][i] != 'F' and df['Grade'][i] != 'I':
                            semwise_credits_cleared[value] += df['Credits'][i]
                        semwise_credits[value] += df['Credits'][i]

                    except:
                        pass
                    i += 1
                for key in keys:
                    try:
                        if semwise_credits_cleared[key] != 0:
                            SPI[key] = round(semwise_score[key] /
                                             semwise_credits_cleared[key], 2)
                        else:
                            SPI[key] = 0
                    except:
                        pass
                i = 0
                for key in keys:
                    try:
                        if i == 0 and i not in back_log:
                            total_credits[key] = semwise_credits[key]
                            total_credits_cleared[key] = semwise_credits[key]
                            x = total_credits[key]
                            y = total_credits_cleared[key]
                        elif i == 0 and i in back_log:
                            total_credits[key] = semwise_credits[key]
                            total_credits_cleared[key] = 0
                            x = total_credits[key]
                            y = total_credits_cleared[key]
                        elif i not in back_log:
                            total_credits[key] += (semwise_credits[key] + x)
                            total_credits_cleared[key] += (
                                semwise_credits[key] + y)
                            x = total_credits[key]
                            y = total_credits_cleared[key]
                        elif i in back_log:
                            total_credits[key] += (semwise_credits[key] + x)
                            x = total_credits[key]
                            total_credits_cleared[key] = y
                    except:
                        pass
                    i += 1
                i = 0
                for key in keys:
                    try:
                        x = 0
                        y = 0
                        for j in sem:
                            x += SPI[j]*semwise_credits_cleared[j]
                        if total_credits_cleared[key] != 0:
                            y = x/total_credits_cleared[key]
                        else:
                            y = 0
                        if str(file) == '1121EE03_individual.csv':
                            print(x, y)
                        CPI[key] = round(y, 2)
                        i += 1
                    except:
                        print(f'Error while working on -> {file}')
                if str(file) == '1121EE03_individual.csv':
                    for key in keys:
                        print(CPI[key])
                data_entry = []
                for key in keys:
                    lst = [sem[key], semwise_credits[key], semwise_credits_cleared[key],
                           SPI[key], total_credits[key], total_credits_cleared[key], CPI[key]]
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


del_create_grades_folder()
roll_number_individual()
roll_number_overall()
