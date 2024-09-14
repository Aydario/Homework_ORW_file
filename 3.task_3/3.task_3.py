def work_with_files(*file_names):
    sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[-1])
    with open('3.task_3\\result.txt', 'w', encoding='utf-8') as result_file:
        for name, length in sorted_file_data:
            result_file.write(name.split("\\")[-1] + '\n')
            result_file.write(f'{length}\n')
            result_file.write(f'{open(name, encoding="utf-8").read()}\n')
            

work_with_files('3.task_3\one.txt', '3.task_3\\two.txt', 
                '3.task_3\\three.txt')
#, 