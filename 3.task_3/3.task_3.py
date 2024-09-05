def work_with_files(f1, f2, f3, resulting_file):
    with open(f1, 'r', encoding='utf8') as file_1, \
            open(f2, 'r', encoding='utf8') as file_2, \
            open(f3, 'r', encoding='utf8') as file_3:
        dict_files = {
            f1: file_1.readlines(),
            f2: file_2.readlines(),
            f3: file_3.readlines()
        }
    with open(resulting_file, 'w', encoding='utf-8') as result:
        for strings in sorted(dict_files.items(), key=lambda x: x[-1], reverse=True):
            name_file, list_strings = strings
            result.write(name_file.split('\\')[-1] + '\n')
            result.write(f'{len(list_strings)}\n')
            result.writelines(list_strings)
            result.write('\n')


work_with_files('3.task_3\one.txt', '3.task_3\\two.txt', 
                '3.task_3\\three.txt', '3.task_3\\result.txt')
