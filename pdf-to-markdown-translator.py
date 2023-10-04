import re
from pdfreader import SimplePDFViewer


def pdf_to_string(pdf_location, page):
    fd = open(pdf_location, "rb")
    viewer = SimplePDFViewer(fd)
    viewer.navigate(page)  # TODO should go through all pages by itself
    viewer.render()
    return viewer.canvas.text_content


def read_line(original):
    return find_string(original), find_position(original)


def find_string(original):
    matches = re.findall(r'\((.*?)\)', original)
    return ''.join(matches)


def find_position(original):
    try:
        return int(re.findall(r'(\d*\d) Tm', original)[0])
    except IndexError:
        return 0


def remove_none_existing_lines(lines_list):  # TODO find solution to empty strings
    """
    DONT USE THIS FUNCTION IT REMOVES IMAGES
    """
    return list(filter(lambda line: line['position'] is not None, lines_list))


def get_headline(lines_list):  # TODO temporary until i figure out the invisible line
    for line in lines_list:
        # Checks if the string is not empty
        if line['string']:
            return line['string']


def write_to_markdown(lines_list):
    # lines_list = remove_none_existing_lines(lines_list)
    headline = get_headline(lines_list)
    with open("my-website/docs/{}.md".format(headline.lower().replace(" ", "-")), "a") as f:
        f.write("---\nsidebar_label: '{0}'\ntitle: '{0}'\n---\n".format(headline))
        previous_pos = 0
        for line in lines_list:
            # Checks if string is not empty
            if line['position'] - previous_pos > 25:
                f.write('\n')
            if line['string']:
                f.write(line['string'])
            if line['position'] != previous_pos:
                f.write('\n')
            previous_pos = line['position']


def text_to_list(pdf_text):
    encoded_lines = pdf_text.split("MCID")
    lines = []
    for line in encoded_lines:
        string, position = read_line(line)
        lines.append({
            'string': string,
            'position': position
        })
    return lines


text = pdf_to_string("./azure-devops-get-started-azure-devops-2022.pdf", 7)
# text = pdf_to_string("./artifactory.pdf", 3)
lines = text_to_list(text)
write_to_markdown(lines)
