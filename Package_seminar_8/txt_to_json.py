'''Возьмите задачу 3 из прошлого семинара, где
создавался текстовый файл.
Напишите функцию, которая создает из этого файла новый с
данными в формате JSON. Имена пишите с большой буквы.
Каждая пара с новой строки.'''

import json
from pathlib import Path

__all__ = ['txt_to_json']

def txt_to_json(file: Path) -> None:
    my_dict = {}
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            name, number = line.split(' ')
            my_dict[name.title()] = float(number)

    with open(f'{file.stem}.json', 'w', encoding='UTF-8')as f_write:
        json.dump(my_dict, f_write, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    txt_to_json(Path('G:\\Мой диск\\СемашкоМА\\Geekbrains\\III ЧЕТВЕРТЬ\\Погружение в Python. Часть 1\\test_seminar7\\result1.txt'))
