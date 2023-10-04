from pdf_to_markdown_translator import *


def get_space_before_above_line(lines_list):
    dict = {}
    previous_pos = 0
    for line in lines_list:
        dict[line['string']] = line['position'] - previous_pos
        previous_pos = line['position']
    return dict


def get_space_dictionary(lines_list):
    lines_space_counter = {}
    previous_pos = 0
    for line in lines_list:
        space = line['position'] - previous_pos
        if not space in lines_space_counter.keys():
            lines_space_counter[space] = 0
        lines_space_counter[space] += 1
        previous_pos = line['position']
    return lines_space_counter


text = pdf_to_string("./azure-devops-get-started-azure-devops-2022.pdf", 7)
lines = text_to_list(text)
print(get_space_before_above_line(lines))
