import os

def count_lines_in_file():


def text_from_files(f):
    text_in_file = []
    for line in f:
        text_in_file.append(line)
        print(text_in_file)
    # return text_in_file


def reads_files():
    fds = sorted(os.listdir())
    files_list = {}
    i = 0
    for file in fds:

        if file.endswith('.txt'):
            file_name = file
            file_path = os.path.join(os.getcwd(), file)
            info_about_file = list()
            i += 1
            text_in_file = []
            with open(file_name, 'r', encoding='utf-8') as f:
                info_file = {}
                count = sum(1 for line in f)
                for line in f:
                    text_in_file.append(line)
                info_file['name_file'], info_file['lines_in_file'], info_file['text'] = file_name, count, text_in_file
                info_about_file.append(info_file)

        files_list[i] = info_about_file
    # sorted_files_list = sorted(files_list, key=lambda x: x['lines_in_file'])
    return files_list
    # print(file_name)
    # print(count)


test = reads_files()
# test = sorted(test[1:], key=lambda x: x['lines_in_file'])
print(test)
