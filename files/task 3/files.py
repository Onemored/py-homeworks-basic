import os

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
            with open(file_name, 'r', encoding='utf-8') as f:
                info_file = {}
                text_in_file = f.readlines()
                count = len(text_in_file)
                info_file['name_file'], info_file['lines_in_file'], info_file['text'] = file_name, count, text_in_file
            info_about_file.append(info_file)
        files_list[i] = info_about_file
    return files_list


test = reads_files()
# test = test.values()
# test = sorted(test, key=lambda x: x['lines_in_file'])
for file in test:
    print(file)
    for info in test[file]:
        print(info)
