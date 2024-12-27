import os


def read_text():
    file_name = os.path.join(os.getcwd(), '1.txt')
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

    # dict = []
    # with open(file_name, 'r', encoding='utf-8') as f:
    #     for line in f:
    #        dict.append(line)
    #     return dict

# config = [];
# with open(filename) as file:
#     for line in file:
#         config.append(line.rstrip());

lines = read_text()
print(lines)