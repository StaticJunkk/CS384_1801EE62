import csv
import os
import re
import shutil
import pandas as pd

direct_path = os.path.join(os.getcwd(), 'grades')

max_sem = {}


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
                max_sem[roll_no] = row['sem']
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
                        back_log.append(i-1)
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
                        print(f'Error while working on -> {file}')
                i = 0
                for value in df['Sem']:
                    try:
                        semwise_score[value] += creds[i]*df['Credits'][i]
                        if df['Grade'][i] != 'F' and df['Grade'][i] != 'I':
                            semwise_credits_cleared[value] += df['Credits'][i]
                        semwise_credits[value] += df['Credits'][i]

                    except:
                        print(f'Error while working on -> {file}')
                    i += 1
                for key in keys:
                    try:
                        if semwise_credits[key] != 0:
                            SPI[key] = round(semwise_score[key] /
                                             semwise_credits[key], 2)
                        else:
                            SPI[key] = 0
                    except:
                        print(f'Error while working on -> {file}')
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
                        print(f'Error while working on -> {file}')
                    i += 1
                i = 0
                for key in keys:
                    try:
                        x = 0
                        y = 0
                        for j in sem:
                            if int(j) <= int(key):
                                x += SPI[j]*semwise_credits[j]
                        if total_credits[key] != 0:
                            y = x/total_credits[key]
                        else:
                            y = 0
                        CPI[key] = round(y, 2)
                        i += 1
                    except:
                        print(f'Error while working on -> {file}')
                data_entry = []
                for key in range(1, int(max_sem[roll_no])+1):
                    if key in keys:
                        lst = [sem[key], semwise_credits[key], semwise_credits_cleared[key],
                               SPI[key], total_credits[key], total_credits_cleared[key], CPI[key]]
                    else:
                        lst = [key, '0', '0', '0', '0', '0', '0']
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
# max_sem = {'0801CS01': '8', '0801CS02': '8', '0801CS03': '8', '0801CS04': '8', '0801CS05': '8', '0801CS06': '8', '0801CS07': '8', '0801CS08': '8', '0801CS09': '8', '0801CS10': '8', '0801CS11': '8', '0801CS12': '8', '0801CS13': '8', '0801CS14': '8', '0801CS15': '8', '0801CS16': '8', '0801CS17': '8', '0801CS18': '8', '0801CS19': '8', '0801CS20': '8', '0801CS21': '8', '0801CS22': '8', '0801CS23': '8', '0801CS24': '8', '0801CS25': '8', '0801CS26': '8', '0801CS27': '8', '0801CS28': '8', '0801CS29': '8', '0801CS30': '8', '0801CS31': '8', '0801CS32': '8', '0801CS33': '8', '0801CS34': '8', '0801CS35': '8', '0801CS36': '8', '0801CS37': '8', '0801CS38': '8', '0801CS39': '8', '0801CS40': '8', '0801EE01': '8', '0801EE02': '8', '0801EE04': '8', '0801EE06': '8', '0801EE08': '8', '0801EE10': '8', '0801EE11': '8', '0801EE12': '8', '0801EE13': '8', '0801EE14': '8', '0801EE15': '8',
#            '0801EE16': '8', '0801EE17': '8', '0801EE18': '8', '0801EE19': '8', '0801EE20': '8', '0801EE21': '8', '0801EE22': '8', '0801EE23': '8', '0801EE24': '8', '0801EE25': '8', '0801EE26': '8', '0801EE29': '8', '0801EE30': '8', '0801EE33': '7', '0801EE34': '8', '0801EE35': '8', '0801ME04': '8', '0801ME05': '8', '0801ME06': '8', '0801ME08': '8', '0801ME09': '8', '0801ME10': '8', '0801ME11': '10', '0801ME12': '8', '0801ME13': '8', '0801ME14': '8', '0801ME16': '8', '0801ME17': '8', '0801ME18': '8', '0801ME19': '8', '0801ME20': '8', '0801ME21': '8', '0801ME22': '8', '0801ME23': '8', '0801ME27': '8', '0801ME28': '8', '0801ME29': '8', '0801ME30': '8', '0801ME32': '8', '0801ME33': '8', '0801ME34': '8', '0901CS01': '8', '0901CS02': '8', '0901CS03': '8', '0901CS04': '8', '0901CS05': '8', '0901CS06': '8', '0901CS07': '8', '0901CS08': '8', '0901CS09': '8', '0901CS10': '5', '0901CS11': '8',
#            '0901CS12': '8', '0901CS13': '8', '0901CS14': '8', '0901CS15': '8', '0901CS16': '8', '0901CS17': '8', '0901CS18': '8', '0901CS19': '8', '0901CS20': '8', '0901CS21': '8', '0901CS22': '8', '0901CS23': '8', '0901CS24': '8', '0901CS25': '8', '0901CS26': '8', '0901CS27': '8', '0901CS28': '8', '0901CS29': '8', '0901CS30': '8', '0901CS31': '8', '0901CS32': '8', '0901CS33': '8', '0901CS34': '2', '0901CS35': '8', '0901CS36': '4', '0901CS37': '8', '0901EE01': '8', '0901EE02': '8', '0901EE03': '8', '0901EE04': '8', '0901EE05': '8', '0901EE06': '8', '0901EE07': '8', '0901EE08': '8', '0901EE09': '8', '0901EE10': '8', '0901EE11': '8', '0901EE12': '8', '0901EE13': '8', '0901EE14': '8', '0901EE15': '8', '0901EE16': '4', '0901EE17': '8', '0901EE18': '8', '0901EE19': '8', '0901EE20': '8', '0901EE21': '8', '0901EE22': '4', '0901EE23': '8', '0901EE24': '8', '0901EE25': '8', '0901EE26': '8', '0901EE28': '8', '0901EE29': '8', '0901EE30': '8', '0901EE31': '8', '0901EE32': '8', '0901EE33': '8', '0901EE34': '8', '0901EE35': '8', '0901EE36': '8', '0901ME01': '8', '0901ME02': '8', '0901ME03': '8', '0901ME04': '8', '0901ME05': '8', '0901ME06': '8', '0901ME07': '8', '0901ME09': '8', '0901ME10': '8', '0901ME11': '8', '0901ME12': '8', '0901ME13': '8', '0901ME14': '8', '0901ME15': '8', '0901ME16': '8', '0901ME17': '8', '0901ME18': '8', '0901ME19': '8', '0901ME20': '8', '0901ME21': '8', '0901ME22': '8', '0921CH01': '1', '0921CH02': '2', '0921CH03': '2', '0921CS01': '2', '0921CS02': '2', '0921CS03': '2', '0921EE01': '2', '0921EE02': '2', '0921HS01': '3', '0921HS02': '3', '0921HS03': '3', '0921HS04':
#            '3', '0921HS05': '2', '0921MA01': '2', '0921MA02': '2', '0921MA03': '2', '0921ME01': '4', '0921ME02': '2', '0921ME03': '2', '0921PH01': '1', '0921PH02': '1', '0921PH03': '1', '1001CS01': '8', '1001CS02': '8', '1001CS03': '8', '1001CS04': '8', '1001CS05': '8', '1001CS06': '8', '1001CS07': '8', '1001CS08': '8', '1001CS09': '8', '1001CS10': '8', '1001CS11': '8', '1001CS12': '8', '1001CS13': '8', '1001CS14': '8', '1001CS15': '8', '1001CS16': '8', '1001CS17': '8', '1001CS18': '8', '1001CS19': '8', '1001CS20': '8', '1001CS21': '8', '1001CS22': '8', '1001CS23': '8', '1001CS24': '8', '1001CS25': '8', '1001CS26': '2', '1001CS27': '8', '1001CS28': '8', '1001CS29': '8', '1001CS30': '8', '1001CS31': '8', '1001CS32': '8', '1001CS33': '8', '1001CS34': '8', '1001CS35': '8', '1001CS36': '8', '1001CS37': '8', '1001CS38': '8', '1001CS39': '8', '1001EE01': '8', '1001EE02': '8', '1001EE03': '8', '1001EE04': '8', '1001EE05': '8', '1001EE06': '8', '1001EE07': '8', '1001EE08': '8', '1001EE09': '8', '1001EE10': '8', '1001EE11': '8', '1001EE12': '8', '1001EE13': '8', '1001EE14': '8', '1001EE15': '8', '1001EE16': '8', '1001EE17': '8', '1001EE18': '8', '1001EE19': '8', '1001EE20': '8', '1001EE21': '8', '1001EE22': '8', '1001EE23': '8', '1001EE24': '8', '1001EE25': '8', '1001EE26': '8', '1001EE27': '8', '1001EE28': '8', '1001EE29': '8', '1001EE30': '8', '1001EE31': '8', '1001EE32': '8', '1001EE33': '8', '1001EE34': '8',
#            '1001EE35': '8', '1001EE36': '8', '1001EE37': '8', '1001EE38': '8', '1001EE39': '8', '1001ME01': '8', '1001ME02': '8', '1001ME03': '8', '1001ME04': '8', '1001ME05': '8', '1001ME06': '8', '1001ME07': '8', '1001ME08': '8', '1001ME09': '8', '1001ME10': '8', '1001ME11': '8', '1001ME12': '8', '1001ME13': '8', '1001ME14': '8', '1001ME15': '8', '1001ME16': '8', '1001ME17': '8', '1001ME18': '8', '1001ME19': '8', '1001ME20': '8', '1001ME21': '8', '1001ME22': '8', '1001ME23': '8', '1001ME24': '8', '1001ME25': '8', '1001ME26': '8', '1001ME27': '8', '1001ME28': '8', '1001ME29': '8', '1001ME30': '8', '1001ME31': '8', '1001ME32': '8', '1001ME33': '8', '1001ME34': '8', '1001ME35': '8', '1001ME36': '8', '1001ME37': '8', '1001ME38': '8', '1001ME39': '8', '1021CH01': '2', '1021CH02': '2', '1021CH03': '2', '1021CH04': '2', '1021CS01': '1', '1021CS02': '2', '1021EE01': '2', '1021EE02': '2', '1021EE03': '2', '1021EE04': '2', '1021EE05': '2', '1021EE06': '2', '1021EE07': '2', '1021EE08': '2', '1021HS01': '2', '1021HS02': '2', '1021MA01': '2', '1021MA02': '1', '1021MA03': '2', '1021ME01': '2', '1021ME03': '2', '1021ME04': '3', '1021ME05': '2', '1021PH01': '2', '1101CS01': '8', '1101CS02': '8', '1101CS03': '8', '1101CS04': '8', '1101CS05': '8', '1101CS06': '8', '1101CS07': '8', '1101CS08': '8', '1101CS09': '8', '1101CS10': '8', '1101CS11': '8', '1101CS12': '8', '1101CS13': '8', '1101CS14': '8', '1101CS15': '8', '1101CS16': '8', '1101CS17': '8', '1101CS18': '8', '1101CS19': '8', '1101CS20': '8', '1101CS21': '8', '1101CS22': '8', '1101CS23': '8', '1101CS24': '8', '1101CS25': '8', '1101CS26':
#            '8', '1101CS27': '8', '1101CS28': '8', '1101CS29': '8', '1101CS30': '8', '1101CS31': '8', '1101CS32': '8', '1101CS33': '8', '1101CS34': '8', '1101CS35': '8', '1101CS36': '8', '1101CS37': '8', '1101CS38': '8', '1101CS39': '8', '1101CS40': '8', '1101EE01': '8', '1101EE02': '8', '1101EE03': '8', '1101EE04': '8', '1101EE05': '8', '1101EE06': '8', '1101EE07': '8', '1101EE08': '8', '1101EE09': '8', '1101EE10': '8', '1101EE11': '8', '1101EE12': '8', '1101EE13': '8', '1101EE15': '8', '1101EE16': '8', '1101EE17': '8', '1101EE19': '8', '1101EE20': '8', '1101EE21': '8', '1101EE22': '8', '1101EE23': '8', '1101EE24': '8', '1101EE25': '8', '1101EE26': '8', '1101EE27': '8', '1101EE28': '8', '1101EE29': '8', '1101EE30': '8', '1101EE31': '8', '1101EE32': '8', '1101EE33': '8', '1101EE34': '8', '1101EE35': '8', '1101EE36': '8', '1101EE37': '8', '1101EE38': '8', '1101EE39': '8', '1101EE40': '8', '1101ME01': '8', '1101ME02': '8', '1101ME03': '8', '1101ME04': '8', '1101ME05': '8', '1101ME06': '8', '1101ME07': '8', '1101ME08': '8', '1101ME09': '8', '1101ME10': '8', '1101ME11': '8', '1101ME12': '8', '1101ME13': '8', '1101ME14': '8', '1101ME15': '8', '1101ME16': '8', '1101ME17': '8', '1101ME18': '8', '1101ME19': '8', '1101ME20': '8', '1101ME21': '8', '1101ME22': '8', '1101ME23': '8', '1101ME24': '8', '1101ME25': '8', '1101ME26': '6', '1101ME27': '8', '1101ME28': '8', '1101ME29': '8', '1101ME30': '8', '1101ME31': '8',
#            '1101ME32': '8', '1101ME33': '8', '1101ME34': '8', '1101ME35': '8', '1101ME36': '8', '1101ME37': '8', '1121CH02': '2', '1121CH03': '3', '1121CH04': '2', '1121CH05': '2', '1121CH06': '2', '1121CH07': '1', '1121CS01': '7', '1121CS02': '2', '1121CS03': '2', '1121CS04': '2', '1121CS05': '3', '1121CS06': '3', '1121CS07': '3', '1121EE01': '2', '1121EE02': '2', '1121EE03': '4', '1121EE04': '4', '1121HS01': '2', '1121HS02': '2', '1121MA01': '2', '1121MA02': '1', '1121MA03': '3', '1121MA04': '2', '1121MA06': '2', '1121MA07': '3', '1121ME01': '3', '1121ME02': '1', '1121ME03': '3', '1121ME04': '1', '1121ME05': '1', '1121PH01': '2', '1121PH02': '3', '1121PH03': '3', '1121PH04': '1', '1121PH05': '3', '1201CS01': '8', '1201CS02': '8', '1201CS03': '8', '1201CS04': '8', '1201CS05': '8', '1201CS06': '8', '1201CS07': '8', '1201CS08': '8', '1201CS09': '8', '1201CS10': '8', '1201CS11': '8', '1201CS12': '8', '1201CS13': '8', '1201CS14': '8', '1201CS15': '8', '1201CS16': '8', '1201CS17': '8', '1201CS18': '8', '1201CS19': '8', '1201CS20': '8', '1201CS21': '8', '1201CS22': '8', '1201CS23': '8', '1201CS24': '8', '1201CS25': '8', '1201CS26': '8', '1201CS27': '8', '1201CS28': '8', '1201CS29': '8', '1201CS30': '8', '1201CS31': '8', '1201CS32': '8', '1201CS33': '8', '1201CS34': '8', '1201CS35': '8', '1201CS36': '8', '1201CS37': '8', '1201CS38': '8', '1201CS39': '8', '1201CS40': '8', '1201CS41': '8', '1201CS42': '8', '1201CS43': '8', '1201CS44': '8', '1201EE01': '8', '1201EE02': '8', '1201EE03': '8', '1201EE04': '8', '1201EE05': '8', '1201EE06': '8', '1201EE08': '8', '1201EE09': '8', '1201EE11':
#            '8', '1201EE12': '8', '1201EE13': '8', '1201EE14': '8', '1201EE15': '8', '1201EE16': '8', '1201EE17': '8', '1201EE18': '8', '1201EE19': '8', '1201EE20': '8', '1201EE21': '8', '1201EE22': '8', '1201EE23': '8', '1201EE24': '8', '1201EE25': '8', '1201EE26': '8', '1201EE27': '8', '1201EE28': '8', '1201EE29': '8', '1201EE30': '8', '1201EE31': '8', '1201EE32': '8', '1201EE33': '8', '1201EE35': '8', '1201EE36': '8', '1201EE37': '8', '1201EE38': '8', '1201EE39': '8', '1201EE40': '8', '1201ME01': '8', '1201ME02': '8', '1201ME03': '8', '1201ME04': '8', '1201ME05': '8', '1201ME06': '8', '1201ME07': '8', '1201ME08': '8', '1201ME09': '8', '1201ME10': '8', '1201ME11': '8', '1201ME12': '8', '1201ME13': '8', '1201ME14': '8', '1201ME15': '8', '1201ME17': '8', '1201ME18': '8', '1201ME20': '8', '1201ME21': '8', '1201ME22': '8', '1201ME23': '8', '1201ME24': '8', '1201ME25': '8', '1201ME26': '8', '1201ME27': '8', '1201ME28': '8', '1201ME29': '8', '1201ME30': '8', '1201ME31': '8', '1201ME32': '8', '1201ME33': '8', '1201ME34': '8', '1201ME35': '8', '1201ME36': '8', '1201ME37': '8', '1201ME38': '8', '1201ME39': '4', '1211MC01': '4', '1211MC02': '4', '1211MC03': '4', '1211MC04': '4', '1211MC05': '4', '1211MC06': '4', '1211MC07': '4', '1211MC08': '4', '1211MC09': '1', '1211MC10': '4', '1211MT01': '4', '1211MT02': '4', '1211MT03': '1', '1211MT04': '4', '1211MT05': '4', '1211MT06': '1', '1211MT07': '1', '1211MT08': '3',
#            '1211MT09': '4', '1211MT10': '1', '1211MT11': '1', '1211NT01': '4', '1211NT02': '4', '1211NT03': '4', '1211NT04': '4', '1211NT05': '4', '1211NT06': '4', '1211NT07': '4', '1211NT08': '4', '1211NT09': '4', '1211NT10': '4', '1221CH01': '1', '1221CS01': '1', '1221CS02': '3', '1221CS03': '1', '1221CS04': '5', '1221CS05': '3', '1221EE01': '3', '1221EE02': '3', '1221HS01': '2', '1221HS02': '2', '1221MA01': '1', '1221MA02': '2', '1221MA03': '2', '1221MA04': '2', '1221MA05': '2', '1221MA06': '2', '1221ME01': '3', '1221ME02': '1', '1221ME03': '2', '1221ME04': '4', '1221MS01': '2', '1221PH02': '2', '1301CE01': '8', '1301CE02': '8', '1301CE03': '8', '1301CE05': '8', '1301CE06': '8', '1301CE07': '8', '1301CE08': '1', '1301CE09': '8', '1301CE10': '8', '1301CE11': '8', '1301CE12': '8', '1301CE13': '8', '1301CE14': '8', '1301CE15': '8', '1301CE16': '8', '1301CE18': '8', '1301CE19': '8', '1301CE20': '8', '1301CE21': '8', '1301CE22': '8', '1301CE23': '8', '1301CH01': '8', '1301CH02': '8', '1301CH03': '8', '1301CH04': '8', '1301CH06': '8', '1301CH07': '8', '1301CH08': '8', '1301CH09': '8', '1301CH10': '8', '1301CH11': '8', '1301CH12': '8', '1301CH13': '8', '1301CH14': '8', '1301CH15': '8', '1301CH16': '8', '1301CH17': '8', '1301CH18': '8', '1301CS02': '8', '1301CS03': '8', '1301CS04': '8', '1301CS05': '8', '1301CS06': '8', '1301CS07': '8', '1301CS08': '8', '1301CS09': '8', '1301CS10': '8', '1301CS11': '8', '1301CS12': '8', '1301CS13': '8', '1301CS14': '8', '1301CS15': '8', '1301CS16': '8', '1301CS17': '8', '1301CS18': '8', '1301CS19': '8', '1301CS20': '8', '1301CS21': '8', '1301CS22':
#            '8', '1301CS23': '8', '1301CS24': '8', '1301CS25': '8', '1301CS26': '8', '1301CS27': '8', '1301CS28': '8', '1301CS29': '8', '1301CS30': '8', '1301CS31': '8', '1301CS32': '8', '1301CS33': '8', '1301CS34': '8', '1301CS35': '8', '1301CS36': '8', '1301CS37': '8', '1301CS38': '8', '1301CS39': '8', '1301CS40': '8', '1301CS41': '8', '1301CS42': '8', '1301CS43': '8', '1301CS44': '8', '1301CS45': '8', '1301CS46': '8', '1301CS47': '8', '1301CS48': '8', '1301CS49': '8', '1301CS50': '8', '1301CS51': '8', '1301CS52': '8', '1301CS53': '8', '1301CS54': '8', '1301CS55': '8', '1301CS56': '8', '1301EE01': '8', '1301EE02': '8', '1301EE03': '8', '1301EE04': '8', '1301EE05': '8', '1301EE06': '8', '1301EE07': '8', '1301EE08': '8', '1301EE09': '8', '1301EE10': '8', '1301EE11': '8', '1301EE12': '8', '1301EE13': '8', '1301EE14': '8', '1301EE15': '8', '1301EE16': '8', '1301EE17': '8', '1301EE18': '8', '1301EE19': '8', '1301EE20': '8', '1301EE21': '8', '1301EE22': '8', '1301EE23': '8', '1301EE24': '8', '1301EE26': '8', '1301EE27': '8', '1301EE28': '8', '1301EE29': '8', '1301EE31': '8', '1301EE32': '8', '1301EE33': '8', '1301EE34': '3', '1301EE35': '8', '1301EE36': '8', '1301EE37': '8', '1301EE38': '8', '1301EE39': '8', '1301EE42': '8', '1301EE43': '8', '1301EE44': '8', '1301EE45': '8', '1301EE46': '7', '1301ME01': '8', '1301ME02': '8', '1301ME03': '8', '1301ME04': '8', '1301ME05': '8', '1301ME06': '8', '1301ME07': '8',
#            '1301ME08': '3', '1301ME09': '8', '1301ME10': '8', '1301ME11': '8', '1301ME12': '8', '1301ME13': '8', '1301ME14': '8', '1301ME15': '8', '1301ME16': '8', '1301ME17': '8', '1301ME19': '8', '1301ME20': '8', '1301ME21': '8', '1301ME22': '8', '1301ME23': '8', '1301ME24': '8', '1301ME25': '8', '1301ME26': '8', '1301ME27': '8', '1301ME28': '8', '1301ME29': '8', '1301ME30': '8', '1301ME31': '8', '1301ME32': '8', '1301ME33': '8', '1301ME34': '8', '1301ME35': '8', '1301ME36': '8', '1301ME37': '8', '1301ME38': '8', '1301ME39': '8', '1301ME40': '8', '1301ME41': '8', '1301ME42': '8', '1301ME43': '8', '1301ME44': '8', '1301ME45': '8', '1301ME46': '8', '1301ME47': '8', '1311CS01': '4', '1311CS02': '4', '1311CS03': '4', '1311CS04': '4', '1311CS05': '4', '1311CS06': '4', '1311CS07': '2', '1311CS08': '4', '1311CS09': '1', '1311CS10': '4', '1311CS11': '4', '1311CS12': '4', '1311CS13': '4', '1311CS14': '4', '1311CS15': '4', '1311EE01': '4', '1311EE02': '4', '1311EE03': '3', '1311EE04': '4', '1311EE05': '4', '1311EE06': '4', '1311EE07': '4', '1311EE08': '4', '1311EE09': '4', '1311EE10': '4', '1311EE11': '4', '1311EE12': '4', '1311EE13': '4', '1311EE14': '4', '1311EE15': '4', '1311EE16': '1', '1311MC01': '4', '1311MC02': '4', '1311MC03': '4', '1311MC04': '1', '1311MC07': '4', '1311MC08': '4', '1311MC09': '1', '1311MC10': '4', '1311MC11': '4', '1311MC12': '4', '1311MC13': '4', '1311MC16': '4', '1311MT01': '3', '1311MT02': '4', '1311MT03': '4', '1311MT04': '4', '1311MT05': '4', '1311MT06': '4', '1311MT07': '4', '1311MT08': '4', '1311MT09': '4', '1311MT10': '4', '1311MT11': '4', '1311MT12':
#            '4', '1311MT13': '2', '1311NT01': '4', '1311NT02': '4', '1311NT03': '4', '1311NT04': '2', '1311NT05': '4', '1311NT06': '4', '1311NT07': '4', '1311NT08': '4', '1311NT09': '1', '1311NT10': '4', '1321CE01': '2', '1321CE02': '2', '1321CE03': '2', '1321CH01': '2', '1321CH02': '2', '1321CH03': '2', '1321CH04': '2', '1321CS01': '3', '1321CS04': '3', '1321CS05': '2', '1321CS06': '1', '1321CS07': '2', '1321EE01': '2', '1321EE02': '2', '1321EE03': '2', '1321EE04': '1', '1321EE05': '1', '1321EE06': '3', '1321EE07': '1', '1321EE08': '1', '1321HS01': '2', '1321HS02': '2', '1321HS03': '2', '1321MA01': '2', '1321ME02': '2', '1321ME03': '4', '1321ME04': '3', '1321ME05': '4', '1321MS01': '1', '1321PH01': '2', '1321PH02': '2', '1321PH03': '2', '1321PH04': '2', '1321PH05': '2'}
roll_number_overall()
