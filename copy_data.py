from return_data_file import data_file

def copy_row():
    data1, nf1 = data_file()
    count_rows = len(data1)
    if count_rows == 0:
        print("Файл пусто!")
    else:
        number_row1 = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row1 < 1 or number_row1 > count_rows:
            number_row1 = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        with open(f'db/data_{nf1}.txt', 'r', encoding='utf-8') as file1:
            lines1 = file1.readlines()
            line_to_copy = lines1[number_row1 - 1] 
        data2, nf2 = data_file()
        # count_rows2 = len(data2)
        last_number2 = int(data2[-1].split(';')[0]) if data2 else 0
        new_number2 = last_number2 + 1
        line_to_copy = f'{new_number2};{line_to_copy.split(';')[1]};{line_to_copy.split(';')[2]};{line_to_copy.split(';')[3]};{line_to_copy.split(';')[4]}'
        data2.append(line_to_copy)
        with open(f'db/data_{nf2}.txt', 'w', encoding='utf-8') as file2:
            file2.writelines(data2)
        print("Строка успешно скопирована!")
