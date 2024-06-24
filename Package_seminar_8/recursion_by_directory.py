'''  Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''

import json
import csv
import pickle
from pathlib import Path

__all__ = ['recursion_by_directory']


def get_dir_size(path: Path) -> int:
    total_size = 0
    for item in path.rglob('*'):
        if item.is_file():
            total_size += item.stat().st_size
    return total_size


def recursion_by_directory(path: Path, parent_dir: str = "") -> list:
    list_write = []
    name = path.name

    for file in path.iterdir():
        dict_write = {}
        dict_write['name'] = file.name
        dict_write['parent_dir'] = parent_dir if parent_dir else name
        if file.is_dir():
            dict_write['type'] = 'dir'
            dict_write['size'] = get_dir_size(file)
            list_write.append(dict_write)
            list_write.extend(recursion_by_directory(file, parent_dir=name))
        else:
            dict_write['type'] = 'file'
            dict_write['size'] = file.stat().st_size
            list_write.append(dict_write)

    return list_write


def save_results(data: list, output_name: str) -> None:
    with open(f'{output_name}.json', 'w', encoding='UTF-8') as f_write_json:
        json.dump(data, f_write_json, indent=2, ensure_ascii=False)

    with open(f'{output_name}.pickle', 'wb') as f_writebytes:
        pickle.dump(data, f_writebytes)

    with open(f'{output_name}.csv', 'w', encoding='utf-8', newline='') as f_write_csv:
        headers_list = data[0].keys() if data else ['name', 'parent_dir', 'type', 'size']
        csv_write = csv.DictWriter(f_write_csv, fieldnames=headers_list, dialect='excel-tab',
                                   quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    base_path = Path('G:\\Мой диск\\СемашкоМА\\Geekbrains\\III ЧЕТВЕРТЬ\\Погружение в Python. Часть 1')
    result_list = recursion_by_directory(base_path)
    save_results(result_list, 'output')
