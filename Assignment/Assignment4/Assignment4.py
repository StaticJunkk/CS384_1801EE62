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


del_create_grades_folder()
roll_number_individual()
