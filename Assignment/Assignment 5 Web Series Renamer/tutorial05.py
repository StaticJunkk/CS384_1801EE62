import os
import re
import shutil


def rename_FIR(folder_name):
    pass


def rename_Game_of_Thrones(folder_name):
    os.chdir(folder_name)
    files = os.listdir(folder_name)
    for file in files:
        info = re.split('-', file)
        series_name, given_number, episode_name_given = info[0], info[1], info[2]
        series_name = series_name.strip()
        given_number = given_number.strip()
        episode_name_given = episode_name_given.strip()
        info = re.split('x', given_number)
        season_number, episode_number = info[0], info[1]
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        if len(season_number) < season_padding:
            season_number = int(int(season_padding) -
                                len(season_number))*'0'+season_number
        if len(episode_number) < episode_padding:
            episode_number = int(int(episode_padding) -
                                 len(episode_number))*'0'+episode_number
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        new_name = series_name + ' - Season ' + \
            season_number + ' Episode '+episode_number + ' - '
        info = re.split('\.', episode_name_given)
        episode_name = info[0]
        extension = info[-1]
        new_name += episode_name + '.' + extension.strip()
        os.rename(file, new_name)


def rename_Sherlock(folder_name):
    os.chdir(folder_name)
    files = os.listdir(folder_name)
    for file in files:
        pattern = re.compile('\d+')
        info = re.split('\.', file)
        number_info = re.findall(pattern, file)
        season_number = number_info[0]
        episode_number = number_info[1]
        if len(season_number) < season_padding:
            season_number = int(int(season_padding) -
                                len(season_number))*'0'+season_number
        if len(episode_number) < episode_padding:
            episode_number = int(int(episode_padding) -
                                 len(episode_number))*'0'+episode_number
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        new_name = info[0]+' - Season '+season_number + \
            ' Episode '+episode_number+'.'+info[-1]
        os.rename(file, new_name)


def rename_Suits(folder_name):
    count = 0
    os.chdir(folder_name)
    files = os.listdir(folder_name)
    for file in files:
        info = re.split('-', file)
        series_name, given_number, episode_name_given = info[0], info[1], info[2]
        series_name = series_name.strip()
        given_number = given_number.strip()
        episode_name_given = episode_name_given.strip()
        info = re.split('x', given_number, maxsplit=2)
        season_number, episode_number = info[0], info[-1]
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        if len(season_number) < season_padding:
            season_number = int(int(season_padding) -
                                len(season_number))*'0'+season_number
        if len(episode_number) < episode_padding:
            episode_number = int(int(episode_padding) -
                                 len(episode_number))*'0'+episode_number
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        new_name = series_name + ' - Season ' + \
            season_number + ' Episode '+episode_number + ' - '
        info = re.split('\.', episode_name_given)
        episode_name = info[0]
        info = re.split('\.', file)
        extension = info[-1]
        new_name += episode_name + '.' + extension.strip()
        try:
            os.rename(file, new_name)
        except:
            print(f"Duplicate file found -> {file}\nDeleting File now")
            os.remove(file)
            print("\n-----------------\nFile Deleted\n")
            count += 1
            continue
    return count


def rename_How_I_Met_Your_Mother(folder_name):
    count = 0
    os.chdir(folder_name)
    files = os.listdir(folder_name)
    for file in files:
        info = re.split('-', file)
        series_name, given_number, episode_name_given = info[0], info[1], info[-1]
        series_name = series_name.strip()
        given_number = given_number.strip()
        episode_name_given = episode_name_given.strip()
        info = re.split('x', given_number)
        season_number, episode_number = info[0], info[-1]
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        if len(season_number) < season_padding:
            season_number = int(int(season_padding) -
                                len(season_number))*'0'+season_number
        if len(episode_number) < episode_padding:
            episode_number = int(int(episode_padding) -
                                 len(episode_number))*'0'+episode_number
        season_number = season_number.strip()
        episode_number = episode_number.strip()
        new_name = series_name + ' - Season ' + \
            season_number + ' Episode '+episode_number + ' - '
        info = re.split('\.', episode_name_given)
        episode_name = info[0]
        extension = info[-1]
        new_name += episode_name + '.' + extension.strip()
        try:
            os.rename(file, new_name)
        except:
            print(f"Duplicate file found -> {file}\nDeleting File now")
            os.remove(file)
            print("\n-----------------\nFile Deleted\n")
            count += 1
            continue
    return count


subtitle_path = os.path.join(os.getcwd(), 'Subtitles')

ch = 0
while ch == 0:
    x = input('''Select the series name:
    1. FIR
    2. Game of Thrones
    3. Sherlock
    4. Suits
    5. How I Met Your Mother
    ''')
    print(type(x))
    valid_entries = ['1', '2', '3', '4', '5']
    if x not in valid_entries:
        print(
            f"\nError: You entered -> {x}\n{x} is an Invalid Entry\nPlease enter a valid entry\n")
    else:
        print('You have entered a valid input\n----------------------------------------\n')
        check_season_padding = 0
        while check_season_padding == 0:
            global season_padding
            season_padding = input(
                "Please select padding for season number -> ")
            try:
                season_padding = float(season_padding)
                check_season_padding = 1
            except:
                print(
                    'Invalid Season Padding\nPlease enter again\n----------------------------------------\n')
        check_episode_padding = 0
        while check_episode_padding == 0:
            global episode_padding
            episode_padding = input(
                "Please select padding for episode number -> ")
            try:
                episode_padding = float(episode_padding)
                check_episode_padding = 1
            except:
                print(
                    'Invalid episode Padding\nPlease enter again\n----------------------------------------\n')
        ch = 1
        if x == '1':
            folder_path = os.path.join(subtitle_path, 'FIR')
            rename_FIR(folder_path)
        elif x == '2':
            folder_path = os.path.join(subtitle_path, 'Game of Thrones')
            rename_Game_of_Thrones(folder_path)
        elif x == '3':
            folder_path = os.path.join(subtitle_path, 'Sherlock')
            rename_Sherlock(folder_path)
        elif x == '4':
            folder_path = os.path.join(subtitle_path, 'Suits')
            deleted_file = rename_Suits(folder_path)
            print(f"Total Duplicate files removed -> {deleted_file}")
        else:
            folder_path = os.path.join(subtitle_path, 'How I Met Your Mother')
            deleted_file = rename_How_I_Met_Your_Mother(folder_path)
            print(f"Total Duplicate files removed -> {deleted_file}")
