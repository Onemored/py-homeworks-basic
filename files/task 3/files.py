import os

def rewrite_file():
    fds = sorted(os.listdir())
    files_list = {}

    for file in fds:
        if file.endswith('.txt'):
            file_name = file
            file_path = os.path.join(os.getcwd(), file)
            out_file = "rewrite_file.txt"
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    dish_name = line.strip()
                    count = int(f.readline())
                    ing_list = list()
            with open(out_file, 'w', encoding='utf-8') as f_total:
                f_total.write(file_name + '\n')
                f_total.write(str(len(file)) + '\n')
                f_total.writelines(file)
                f_total.write('\n')
            print(file)
            print(f_total)


rewrite_file()