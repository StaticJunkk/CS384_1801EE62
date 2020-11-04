with open(file_path, 'a+', newline='') as file:
                file.write(f'Roll: {roll_no}')
                file.write('Semester Wise Details')
                writer = csv.DictWriter(file, fieldnames=[
                                        'Subject', 'Credits', 'Type', 'Grade', 'Sem'])
                writer.writeheader()
                # writer.writerow(row)
                file.close()