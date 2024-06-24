'''Прочитайте csv из прошлого задания без
испольщования Dict.Reader
Дополните id до 10 цифр незначащими нулями.
Первую букву имиени сделайте прописной
Добавьте поле хэш на основе имени и идентификатора
Получившиеся записи сохрание в json файл , где каждая
строка csv файла представлена как отделный json словарь
Имя исходноого и конецного файла передавайте как аргументы
функции'''


import csv
import json
from pathlib import Path

__all__ = ['csv_to_json']


def csv_to_json(csv_file: Path, json_file: Path) -> None:
    json_list = []
    with open(csv_file, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            json_dict = {}
            if i != 0:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(id):010}'
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)

    with open(json_file, 'w', encoding='utf-8') as f_write:
        json.dump(json_list, f_write, indent=2)


if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_users.json'))