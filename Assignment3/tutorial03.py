import csv
import os
import re
import shutil
os.system('cls')
# setting the current working directory to access the csv file
path = os.getcwd()
# creating variable with path to analytics folder
direct_path = os.path.join(path, r'analytics')


# function to delete analytics folder in the beginning to avoid overfilling files
def del_create_analytics_folder():
    if os.path.isdir(direct_path):
        shutil.rmtree(direct_path)
    # creating fresh empty analytics folder
    os.mkdir(direct_path)


def course():                                              # creating course function
    dir_path = os.path.join(direct_path, r'course')
    # checking if folder exists, else creating it again
    if os.path.isdir(dir_path):
        pass
    else:
        os.mkdir(dir_path)
    courses = []
    # creating list for categories to be matched with numerical code in roll number
    course_type = ['btech', 'mtech', 'msc', 'phd']
    try:
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                roll_no = row['id']
                # checking pattern for roll no, else sending the row to misc.csv
                pattern = re.compile(r'^[0-9]{4}[A-Z]{2}[0-9]{2}$')
                if re.match(pattern, roll_no):
                    # splitting roll number into elements
                    year = roll_no[0:2]
                    course_type = roll_no[2:4]
                    branch_name = roll_no[4:6]
                    serial_no = roll_no[6:8]
                    pattern = re.compile(branch_name)
                    check_pass = 0
                    new_path = os.path.join(dir_path, branch_name.lower())
                    for course in courses:
                        # checking if branch name is found in the course list
                        if re.match(pattern, course):
                            check_pass = 1
                            break
                    if check_pass == 1:
                        pass
                    # if new course name is encountered, course list is appended, new folder is created
                    else:
                        if os.path.isdir(new_path):
                            pass
                        else:
                            os.mkdir(new_path)
                            courses.append(branch_name)

                    # checking for each particular type of course corresponding to the numerical code obtained
                    pattern = re.compile(r'01')
                    if re.match(pattern, course_type):
                        course_name = 'btech'
                        type_path = os.path.join(new_path, 'btech')
                        # print(type_path)
                        # checking if the course_tpye directory exists, if not, creating new directory
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    pattern = re.compile(r'11')
                    if re.match(pattern, course_type):
                        course_name = 'mtech'
                        type_path = os.path.join(new_path, 'mtech')
                        # print(type_path)
                        # checking if the course_tpye directory exists, if not, creating new directory
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    pattern = re.compile(r'12')
                    if re.match(pattern, course_type):
                        course_name = 'msc'
                        type_path = os.path.join(new_path, 'msc')
                        # print(type_path)
                        # checking if the course_type directory exists, if not, creating new directory
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    pattern = re.compile(r'21')
                    if re.match(pattern, course_type):
                        course_name = 'phd'
                        type_path = os.path.join(new_path, 'phd')
                        # print(type_path)
                        # checking if the course_tpye directory exists, if not, creating new directory
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                    file_name = year+'_'+branch_name.lower()+'_'+course_name + \
                        '.csv'  # creating corresponding file name
                    file_path = os.path.join(type_path, file_name)
                    if os.path.isfile(file_path):
                        # opening file in append mode, then writing the current row, with header
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

                else:                                                    # adding invalid roll numbers to misc.csv
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


def country():                                                # segregating data w.r.t country
    try:
        dir_path = os.path.join(direct_path, r'country')
        # checking  if country directory exists, else creating a new one
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                country_name = row['country']
                if country_name == '':                        # if country field is empty, then naming the file as misc.csv
                    file_name = 'misc.csv'

                else:
                    # else, setting the file name to corresponding country name
                    file_name = country_name.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                # adding row to corresponding csv, with header
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


def email_domain_extract():                                   # segregating data w.r.t email domain name
    try:
        dir_path = os.path.join(direct_path, r'email_domain')
        # checking if email_domain folder, else creating new directory
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                email_id = row['email']
                # if email field is empty, then setting email such that file created is misc.csv
                if email_id is '':
                    email_id = 'misc@misc.com'
                user_id, domain_id = re.split(
                    r'@', email_id)     # splitting w.r.t @
                # splitting w.r.t ., first string obtained is the domain_name
                domain_id_components = re.split(r'\.', domain_id)
                domain_name = domain_id_components[0]
                file_name = domain_name.lower() + '.csv'
                file_path = os.path.join(dir_path, file_name)
                # writing csv file corrosponding to the domain name with header
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


def gender():                                 # segregating data w.r.t gender name
    try:
        dir_path = os.path.join(direct_path, r'gender')
        # checking if gender folder exists, else creating new directory
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                # if gender field is empty, then setting gender such that file created is misc.csv
                gender_type = row['gender']
                if gender_type == '':
                    file_name = 'misc.csv'
                else:
                    file_name = gender_type.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                # writing csv file corrosponding to the gender with header
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


def dob():                  # segregating data w.r.t dob domain name
    try:
        # checking if dob folder exists, else creating new directory
        dir_path = os.path.join(direct_path, r'dob')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                birth_date = row['dob']
                # splitting birth date for date, month and year
                date, month, year = re.split(r'-', birth_date)

                # entering data corresponding to each category
                if int(year) <= 1999 and int(year) >= 1995:

                    file_name = 'bday_1995_1999.csv'
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        # writing csv file corrosponding to the year category with header
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
                        # writing csv file corrosponding to the year category with header
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
                        # writing csv file corrosponding to the year category with header
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
                        # writing csv file corrosponding to the year category with header
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
                        # writing csv file corrosponding to the year category with header
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
                        # writing csv file corrosponding to the year category with header
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


def state():                 # segregating data w.r.t state name
    try:
        # checking if state folder exists, else creating new directory
        dir_path = os.path.join(direct_path, r'state')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                # if state field is empty, then setting name such that file created is misc.csv
                state_name = row['state']
                if state_name == '':
                    file_name = 'misc.csv'

                else:
                    file_name = state_name.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    # writing csv file corrosponding to the state name with header
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


def blood_group():              # segregating data w.r.t blood_groups
    try:
        dir_path = os.path.join(direct_path, r'blood_group')
        if os.path.isdir(dir_path):
            pass
        else:
            os.mkdir(dir_path)
        # checking if blood_group folder exists, else creating new directory
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                # if blood_group field is empty, then setting blood_group such that file created is misc.csv
                blood_grp = row['blood_group']
                if blood_grp == '':
                    file_name = 'misc.csv'

                else:
                    file_name = blood_grp.lower() + '.csv'

                file_path = os.path.join(dir_path, file_name)
                if os.path.isfile(file_path):
                    # writing csv file corrosponding to the blood_group with header
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
        fields = ['id', 'full_name', 'country', 'email',                   # setting fields as per the old data
                  'gender', 'dob', 'blood_group', 'state']
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            for row in reader:
                copy_row = row.copy()
                first_name, last_name = re.split(
                    r' ', row['full_name'], maxsplit=1)                     # splitting full name into first and last names
                del(copy_row['full_name'])
                copy_row['first_name'] = first_name
                copy_row['last_name'] = last_name
                file_name = 'studentinfo_cs384_names_split.csv'
                field_names = ['id', 'first_name', 'last_name', 'country',              # setting new fields_names
                               'email', 'gender', 'dob', 'blood_group', 'state']
                file_path = os.path.join(dir_path, file_name)
                # writing new data into file with fieldnames as header
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
            # sorting the list obtained
            sorted_list = sorted(reader, key=lambda row: row[1])
            file.close()
        file_name = 'studentinfo_cs384_names_split_sorted_first_name.csv'
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):  # writing the file with header
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
