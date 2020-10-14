import csv
import os
import re
os.system('cls')
path = os.getcwd()


def course():
    dir_path = os.path.join(path, r'analytics\course')
    courses = []
    course_type = ['btech', 'mtech', 'msc', 'phd']
    try:
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)

            for row in reader:
                roll_no = row['id']
                pattern = re.compile(r'[0-9]{4}[A-Z]{2}[0-9]{2}')
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
                    # print(course_type)
                    pattern = re.compile(r'01')
                    if re.match(pattern, course_type):
                        type_path = os.path.join(new_path, 'btech')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)
                    pattern = re.compile(r'11')
                    if re.match(pattern, course_type):
                        type_path = os.path.join(new_path, 'mtech')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)
                    pattern = re.compile(r'12')
                    if re.match(pattern, course_type):
                        type_path = os.path.join(new_path, 'msc')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)
                    pattern = re.compile(r'21')
                    if re.match(pattern, course_type):
                        type_path = os.path.join(new_path, 'phd')
                        # print(type_path)
                        if os.path.isdir(type_path):
                            pass
                        else:
                            os.mkdir(type_path)

                else:
                    pass

    except:
        print('Error while reading CSV file')


course()

# def country():
#     # Read csv and process
#     pass


# def email_domain_extract():
#     # Read csv and process
#     pass


# def gender():
#     # Read csv and process
#     pass


# def dob():
#     # Read csv and process
#     pass


# def state():
#     # Read csv and process
#     pass


# def blood_group():
#     # Read csv and process
#     pass


# # Create the new file here and also sort it in this function only.
# def new_file_sort():
#     # Read csv and process
#     pass
