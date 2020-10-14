import csv
import os
import re
os.system('cls')
path = os.getcwd()


def course():
    dir_path = os.path.join(path, r'analytics\course')
    courses = ('cs', 'ee', 'me', 'cb', 'ce', 'ms', 'ph',
               'ma', 'hs', 'ch', 'nt', 'mt', 'ms', 'mc')
    course_type = ('btech', 'mtech', 'msc', 'phd')
    for course_name in courses:
        new_path = os.path.join(dir_path, course_name)
        if os.path.exists(new_path):
            for types in course_type:
                inner_path = os.path.join(new_path, types)
                if os.path.exists(inner_path):
                    pass
                else:
                    os.mkdir(inner_path)
        else:
            os.mkdir(new_path)
            new_path = os.path.join(dir_path, course_name)
        if os.path.exists(new_path):
            for types in course_type:
                inner_path = os.path.join(new_path, types)
                if os.path.exists(inner_path):
                    pass
                else:
                    os.mkdir(inner_path)
    try:
        with open('studentinfo_cs384.csv', 'r') as info_file:
            reader = csv.DictReader(info_file)
            # for rows in reader:
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
