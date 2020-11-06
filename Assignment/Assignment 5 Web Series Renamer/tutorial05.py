def rename_FIR(folder_name):
    pass


def rename_Game_of_Thrones(folder_name):
    pass


def rename_Sherlock(folder_name):
    pass


def rename_Suits(folder_name):
    pass


def rename_How_I_Met_Your_Mother(folder_name):
    pass


ch = 0
while ch == 0:
    x = input('''Select the series name:
    1. FIR
    2. Game of Thrones
    3. Sherlock
    4. Suits
    5. How I Met Your Mother
    ''')

    valid_entries = ['1', '2', '3', '4', '5']
    if x not in valid_entries:
        print(
            f"\nError: You entered -> {x}\n{x} is an Invalid Entry\nPlease enter a valid entry\n")
    else:
        ch = 1
        if x == 1:
            rename_FIR
        elif x == 2:
            rename_Game_of_Thrones
        elif x == 3:
            rename_Sherlock
        elif x == 4:
            rename_Suits
        else:
            rename_How_I_Met_Your_Mother
