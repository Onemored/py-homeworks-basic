import os


def read_cookbook():
    file_name = os.path.join(os.getcwd(), '1.txt')
    dict = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
           dict.append(line)
        return dict

# config = [];
# with open(filename) as file:
#     for line in file:
#         config.append(line.rstrip());

dict = read_cookbook()
print(dict)