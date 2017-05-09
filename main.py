import os
import queries
import psycopg2


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    if os.name == 'nt':
        os.system('cls')


def print_data(data):
    '''Pretty prints data given to it. Presumes that the data parameter
    is a nested list: data[0] = list of column names, data[1] = list of tuples
    each tuple represents a row to be printed'''
    clear_screen()
    column_widths = []
    total_width = 0
    # Determine how wide the printed table needs to be
    # Builds a list, where each element is the width of a column to be printed
    for column_name in data[0]:
        column_widths.append(len(column_name))

    for row in data[1]:
        for index, column in enumerate(row):
            if column_widths[index] < len(str(column)):
                column_widths[index] = len(str(column))

    # total_width only used to print a separating line under the column names
    for number in column_widths:
        total_width += (number + 2)

    # Print column names
    for index, column_name in enumerate(data[0]):
        print(str(data[0][index]).rjust(column_widths[index]), end="  ")
    # Print separating line
    print("\n" + "=" * (total_width))
    # Print the rows of data
    for row in data[1]:
        for index, column in enumerate(row):
            print(str(column).rjust(column_widths[index]), end="  ")
        print("")


def menu():
    '''Function to handle the menu and navigate the various queries'''
    menu_options = ['List mentor names',
                    'List mentor nicknames',
                    'Find applicant "Carol"',
                    'Find applicant by email',
                    'Insert new applicant Markus',
                    'Update applicant tel nr, Jemima',
                    'Delete applicants by email',
                    'Display mentors table',
                    'Display applicants table']
    for index, menu_item in enumerate(menu_options):
        print(str(index + 1), "-", str(menu_item))
    print("0 - Exit")

    valid_option = False
    choice = 0
    while not valid_option:
        try:
            choice = int(input("Please enter chosen menu option: "))
        except ValueError:
            print('Chosen option must be a number between 0 and 9')
            continue
        if choice >= 0 and choice <= 9:
            valid_option = True
        else:
            print('Chosen option must be a number between 0 and 9')

    if choice == 0:
        print('\n')
        print('exiting...')
        quit()
    elif choice == 1:
        print_data(queries.mentor_name())
        print('\n')
        input('Press enter to return to menu')
    elif choice == 2:
        print_data(queries.mentor_nicks())
        print('\n')
        input('Press enter to return to menu')
    elif choice == 3:
        print_data(queries.applicant_carol())
        print('\n')
        input('Press enter to return to menu')
    elif choice == 4:
        print_data(queries.find_applicant_by_email())
        print('\n')
        input('Press enter to return to menu')
    elif choice == 5:
        try:
            print_data(queries.new_applicant_insert_select())
        except psycopg2.IntegrityError as err:
            print(err)
        print('\n')
        input('Press enter to return to menu')
    elif choice == 6:
        print_data(queries.jemima_tel_nr_update())
        print('\n')
        input('Press enter to return to menu')
    elif choice == 7:
        print_data(queries.delete_by_email())
        print('\n')
        input('Press enter to return to menu')
    elif choice == 8:
        print_data(queries.show_mentors())
        print('\n')
        input('Press enter to return to menu')
    elif choice == 9:
        print_data(queries.show_applicants())
        print('\n')
        input('Press enter to return to menu')


def main():
    while True:
        clear_screen()
        menu()


if __name__ == '__main__':
    main()