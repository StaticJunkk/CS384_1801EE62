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
                if (len(roll_no) == 8):
                    year = roll_no[0:2]
                    course_type = roll_no[2:4]
                    branch_name = roll_no[4:6]
                    serial_no = roll_no[6:8]
                    pattern = re.compile(branch_name)
                    check_pass = 0

                    for course in courses:
                        if re.match(pattern, course):
                            check_pass = 1
                            break

                    if check_pass == 1:
                        pass
                    else:
                        new_path = os.path.join(dir_path, branch_name.lower())
                        # print(new_path)
                        if os.path.exists(new_path):
                            pass
                        else:
                            os.mkdir(new_path)
                            courses.append(branch_name)
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
