# student_db =
# student_db is a data structure that contains information about student

import datetime , csv , sys , os

# student_db = {}

def get_user_input():
    '''This will take a user command and then call the dispatcher'''

    while True:
        user_input = []
        user_input = input("Insert Command :")
        user_input_split = user_input.split()
        dispatcher(user_input)
        if (user_input_split[0] == 'exit'):
            exit_func()
            return
    return


def dispatcher(cmd_string):
    '''Takes a user command and then calls a corresponding function'''

    cmd_string_split = cmd_string.split()
    #
    # func_to_call = function(cmd_string_split[0])
    #
    if (cmd_string_split[0] == 'add'):
        add_func(cmd_string_split[1::])
    if (cmd_string_split[0] == 'del'):
        del_func(cmd_string_split[1::])
    if (cmd_string_split[0] == 'find'):
        find_func(cmd_string_split[1::])
    #
    # func_to_call(cmd_string_split)
    #

    return


# Add function
def add_func(user_data):
    print("Added:", user_data)
    student_db = user_data
    # calling file writer
    file_writer('studentdb.dat', user_data)
    # calling log writer
    log_action("User Added:", user_data)
    return


# Find User Function
def find_func(user_data):
    listUser = []

    listUser = list(student_db[user_data])

    print("Find:", listUser)

    return


# Delete User Function
def del_func(user_data):
        del student_db[user_data]
        print("Del:")
        log_action("Deleted:", user_data)
        return


# Average User Function
def avg_func():
    for avg in student_db.values():
        expertise_ = student_db.get()
    return


# Exit Function
def exit_func():
    print("Good Bye:")
    return


# Logs Activity in file
def log_action(action_, string_):
    dt = datetime.datetime.now()
    string_ = [dt, action_, string_]
    filename_ = "studentdb.log"
    file_writer(filename_, string_)
    return



def file_writer(filename_, string_):
            with open(filename_, 'a') as o_file:
                 my_csv_writer = csv.writer(o_file, delimiter=',')
                 my_csv_writer.writerow( [ string_ ])
            return


def reader_reader(filename_, string_):
            with open(filename_, 'r') as o_file:
                my_csv_reader = csv.reader(o_file, delimiter=',')
                my_csv_reader.readrow(string_)
            return
