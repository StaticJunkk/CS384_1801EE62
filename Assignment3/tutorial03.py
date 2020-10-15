import csv
import os
import re
import shutil
os.system('cls')
path = os.getcwd()
direct_path = os.path.join(path, r'analytics')


def del_create_analytics_folder():
    if os.path.isdir(direct_path):
        shutil.rmtree(direct_path)
    os.mkdir(direct_path)


# if os.path.isdir(direct_path):
#     pass
# else:


def course():
    dir_path = os.path.join(direct_path, r'course')
    if os.path.isdir(dir_path):
        pass
    else:
        os.mkdir(dir_path)
    courses = []
    course_type = ['btech', 'mtech', 'msc', 'phd']
    try:
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                roll_no = row['id']
                pattern = re.compile(r'^[0-9]{4}[A-Z]{2}[0-9]{2}$')
                if re.match(pattern, roll_no):
                    year = roll_no[0:2]
                    course_type = roll_no[2:4]
                    branch_name = roll_no[4:6]
                    serial_no = roll_no[6:8]
                    pattern = re.compile(branch_name)
                    check_pass = 0
                    new_path = os.path.join(dir_path, branch_name.lower())
                    for course in courses:
                        if re.match(pattern, course):
                            check_pass = 1
                            break
                    if check_pass == 1:
                        pass
                    else:
                        if os.path.isdir(new_path):
                            pass
                        else:
                            os.mkdir(new_path)
                            courses.append(branch_name)

                    pattern = re.compile(r'01')
                    if re.match(pattern, course_type):
                        course_name = 'btech'
                        type_path = os.path.join(new_path, 'btech')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    pattern = re.compile(r'11')
                    if re.match(pattern, course_type):
                        course_name = 'mtech'
                        type_path = os.path.join(new_path, 'mtech')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    pattern = re.compile(r'12')
                    if re.match(pattern, course_type):
                        course_name = 'msc'
                        type_path = os.path.join(new_path, 'msc')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    pattern = re.compile(r'21')
                    if re.match(pattern, course_type):
                        course_name = 'phd'
                        type_path = os.path.join(new_path, 'phd')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    file_name = year+'_'+branch_name.lower()+'_'+course_name+'.csv'
                    file_path = os.path.join(type_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

                else:
                    misc_path = os.path.join(dir_path, 'misc.csv')

                    if os.path.isfile(misc_path):
                        with open(misc_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(misc_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

    except:
        print('Error while reading CSV file')


def country():
    try:
        dir_path = os.path.join(direct_path, r'country')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                country_name = row['country']
                if country_name == '':
                    file_name = 'misc.csv'

                else:
                    file_name = country_name.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writerow(row)
                        file.close()
                else:
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writeheader()
                        writer.writerow(row)
                        file.close()

    except:
        print("Error in reading CSV file")


def email_domain_extract():
    try:
        dir_path = os.path.join(direct_path, r'email_domain')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                email_id = row['email']
                if email_id is '':
                    email_id = 'misc@misc.com'
                user_id, domain_id = re.split(r'@', email_id)
                domain_id_components = re.split(r'\.', domain_id)
                domain_name = domain_id_components[0]
                file_name = domain_name.lower() + '.csv'
                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writerow(row)
                        file.close()
                else:
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writeheader()
                        writer.writerow(row)
                        file.close()

    except:
        print("Error in reading CSV file")


def gender():
    try:
        dir_path = os.path.join(direct_path, r'gender')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                gender_type = row['gender']
                if gender_type == '':
                    file_name = 'misc.csv'
                else:
                    file_name = gender_type.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writerow(row)
                        file.close()
                else:
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writeheader()
                        writer.writerow(row)
                        file.close()

    except:
        print("Error in reading CSV file")


def dob():
    try:
        dir_path = os.path.join(direct_path, r'dob')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                birth_date = row['dob']
                date, month, year = re.split(r'-', birth_date)

                if int(year) <= 1999 and int(year) >= 1995:

                    file_name = 'bday_1995_1999.csv'
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

                elif int(year) <= 2004 and int(year) >= 2000:
                    file_name = 'bday_2000_2004.csv'
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

                elif int(year) <= 2009 and int(year) >= 2005:
                    file_name = 'bday_2005_2009.csv'
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

                elif int(year) <= 2014 and int(year) >= 2010:
                    file_name = 'bday_2010_2014.csv'
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

                elif int(year) <= 2020 and int(year) >= 2015:
                    file_name = 'bday_2015_2020.csv'
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

                else:
                    file_name = 'misc.csv'
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writerow(row)
                            file.close()
                    else:
                        with open(file_path, 'a+', newline='') as file:
                            writer = csv.DictWriter(file, fieldnames=[
                                                    'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                            writer.writeheader()
                            writer.writerow(row)
                            file.close()

    except:
        print("Error in reading CSV file")


def state():
    try:
        dir_path = os.path.join(direct_path, r'state')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                state_name = row['state']
                if state_name == '':
                    file_name = 'misc.csv'

                else:
                    file_name = state_name.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writerow(row)
                        file.close()
                else:
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writeheader()
                        writer.writerow(row)
                        file.close()

    except:
        print("Error in reading CSV file")


def blood_group():
    try:
        dir_path = os.path.join(direct_path, r'blood_group')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                blood_grp = row['blood_group']
                if blood_grp == '':
                    file_name = 'misc.csv'

                else:
                    file_name = blood_grp.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writerow(row)
                        file.close()
                else:
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=[
                                                'id', 'full_name', 'country', 'email', 'gender', 'dob', 'blood_group', 'state'])
                        writer.writeheader()
                        writer.writerow(row)
                        file.close()
    except:
        print("Error in reading CSV file")


# # Create the new file here and also sort it in this function only.
def new_file_sort():
    try:
        dir_path = direct_path
        fields = ['id', 'full_name', 'country', 'email',
                  'gender', 'dob', 'blood_group', 'state']
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                copy_row = row.copy()
                first_name, last_name = re.split(
                    r' ', row['full_name'], maxsplit=1)
                del(copy_row['full_name'])
                copy_row['first_name'] = first_name
                copy_row['last_name'] = last_name
                file_name = 'studentinfo_cs384_names_split.csv'
                field_names = ['id', 'first_name', 'last_name', 'country',
                               'email', 'gender', 'dob', 'blood_group', 'state']
                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writerow(copy_row)
                        file.close()
                else:
                    with open(file_path, 'a+', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerow(copy_row)
                        file.close()
        file_name = 'studentinfo_cs384_names_split.csv'
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'r') as info_file:
            reader = csv.reader(info_file)
            sorted_list = sorted(reader, key=lambda row: row[1])
            file.close()
        file_name = 'studentinfo_cs384_names_split_sorted_first_name.csv'
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(sorted_list[:-1])
                file.close()
        else:
            with open(file_path, 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(field_names)
                writer.writerows(sorted_list[:-1])
                file.close()

    except:
        print("Error in reading CSV file")


# del_create_analytics_folder()
# course()
# country()
# gender()
# email_domain_extract()
# dob()
# state()
# blood_group()
# new_file_sort()
