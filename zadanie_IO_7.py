"""
 Write a program that given a text file will create a new text file in which all
 the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).
"""


def number_lines_in_file(filename):
    with open(filename, 'r+') as f:
        file_content = f.readlines()

        for index in range(len(file_content)):
            file_content[index] = "{} {}".format(index+1, file_content[index])

        f.seek(0)
        f.writelines(file_content)


number_lines_in_file('test_file_for_exe_IO_7.txt')
