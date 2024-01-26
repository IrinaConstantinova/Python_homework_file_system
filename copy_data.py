from return_data_file import data_file

def copy_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        
        with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file1:
            lines_file1 = file1.readlines()
            line_to_copy = data[number_row - 1]
            file1.readline(line_to_copy)
        data, nf = data_file()
        with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file2:
            lines_file2 = file2.readlines()
            last_number = int(lines_file2[-1].split(';')[0]) if lines_file2 else 0
        with open(f'db/data_{nf}.txt', 'a', encoding='utf-8') as file2:
            for line in lines_file1:
                last_number += 1
                new_line = f'{last_number} {line.split(maxsplit=1)[1]}'
                file2.write(new_line)

        
        print("Строка успешно скопирована!")