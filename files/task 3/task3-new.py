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
                my_count = len(text_in_file)
                info_file['name_file'], info_file['lines_in_file'], info_file[
                    'text'] = file_name, my_count, text_in_file
            files_list.append(info_file)
    return files_list


def write_file():
    list_dictonaries = reads_files()
    list_dictonaries = sorted(list_dictonaries, key=lambda x: x['lines_in_file'])
    out_file = "rewrite_file.txt"
    file_path = os.path.join(os.getcwd(), out_file)
    with open(file_path, 'w', encoding='utf-8') as f_total:
        for dictonary in list_dictonaries:
            f_total.write(f'{dictonary['name_file']}\n{dictonary['lines_in_file']}\n{''.join(dictonary['text'])}\n')
        return f_total


write_file()
