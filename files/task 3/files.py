import os

def reads_files():
    fds = sorted(os.listdir())
    files_list = {}

    for file in fds:
        if file.endswith('.txt'):
            file_name = file
            file_path = os.path.join(os.getcwd(), file)
            with open(file_name, 'r', encoding='utf-8') as f:
                count = sum(1 for line in f)









def open_file():
    pass



            # with open(out_file, 'w', encoding='utf-8') as f_total:
            #     f_total.write(file_name + '\n')
            #     f_total.write(str(len(file)) + '\n')
            #     f_total.writelines(file)
            #     f_total.write('\n')
            # print(file)
            # print(f_total)


reads_files()