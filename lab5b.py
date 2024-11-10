#!/usr/bin/env python3
# Author ID: ggairhe

def read_file_string(file_name):
    """Takes a file_name as a string for a file name, returns its entire contents as a string."""
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    """Takes a file_name as a string for a file name, returns its entire contents as a list of lines without new-line characters."""
    with open(file_name, 'r') as file:
        return [line.rstrip('\n') for line in file]

def append_file_string(file_name, string_of_lines):
    """Takes two strings, appends the string to the end of the file."""
    with open(file_name, 'a') as file:
        file.write(string_of_lines)


def write_file_list(file_name, list_of_lines):
    """Takes a string and list, writes all items from list to file where each item is one line."""
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n') 
def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Takes two strings, reads data from the first file, writes data to a new file, adds line numbers to new file."""
    with open(file_name_read, 'r') as read_file:
        with open(file_name_write, 'w') as write_file:
            line_number = 1
            for line in read_file:
                write_file.write(f"{line_number}:{line}")
                line_number += 1

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)  
    print(read_file_string(file1)) 

    write_file_list(file2, list1) 
    print(read_file_string(file2)) 

    copy_file_add_line_numbers(file2, file3) 
    print(read_file_string(file3))  
