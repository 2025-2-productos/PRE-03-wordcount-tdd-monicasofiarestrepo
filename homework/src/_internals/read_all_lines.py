import os


def read_all_lines(input_folder):

    lines = []
    for filename in os.listdir(input_folder):
        with open(os.path.join(input_folder, filename), "r") as file:
            lines.extend(file.readlines())

    return lines
