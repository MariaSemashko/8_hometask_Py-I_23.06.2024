'''Напишите функцию, которая ищет json файлы
в указанной лиректории и сохраняет их содержимое в
виде одноименных pickle файлов.
'''


import json
import pickle
from pathlib import Path

__all__ = ['json_to_pickle']


def json_to_pickle(path: Path) -> None:
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(file, 'r', encoding='utf-8') as f_read:
                data = json.load(f_read)
            with open(f'{file.stem}.pickle', 'wb') as f_writebytes:
                pickle.dump(data, f_writebytes)


if __name__ == '__main__':
    json_to_pickle(Path('G:\\Мой диск\\СемашкоМА\\Geekbrains\\III ЧЕТВЕРТЬ\\Погружение в Python. Часть 1'))


