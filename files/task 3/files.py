import os


def reads_files():
    fds = sorted(os.listdir())
    files_list = []
    for file in fds:

        if file.endswith('.txt'):
            file_name = file
            file_path = os.path.join(os.getcwd(), file)
            with open(file_path, 'r', encoding='utf-8') as f:
                info_file = {}
                text_in_file = f.readlines()
                count = len(text_in_file)
                info_file['name_file'], info_file['lines_in_file'], info_file['text'] = file_name, count, text_in_file
            files_list.append(info_file)
    return files_list

def write_file():
    list_dictonaries = reads_files()
    list_dictonaries = sorted(test, key=lambda x: x['lines_in_file'])
    print(list_dictonaries)
    # out_file = "rewrite_file.txt"
    # file_path = os.path.join(os.getcwd(), file)
    # with open(file_path, 'w', encoding='utf-8') as f_total:
    #     f_total.write(path1 + '\n')
    #     f_total.write(str(len(file1)) + '\n')
    #     f_total.writelines(file1)
    #     f_total.write('\n')



    return list_dictonaries


test1 = reads_files()
test = write_file()
print(test)
print(test1)
