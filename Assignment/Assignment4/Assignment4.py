import csv
import os
import re
import shutil

direct_path = os.path.join(os.getcwd(), 'grades')


def del_create_grades_folder():
    if os.path.isdir(direct_path):
        shutil.rmtree(direct_path)
    # creating fresh empty grades folder
    os.mkdir(direct_path)


del_create_grades_folder()
