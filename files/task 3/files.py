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
                count = sum(1 for line in f)
                info_file['name_file'], info_file['lines_in_file'] = file_name, count
                info_about_file.append(info_file)


        files_list[i] = info_about_file
    return files_list
            # print(file_name)
            # print(count)

test = reads_files()
print(test)