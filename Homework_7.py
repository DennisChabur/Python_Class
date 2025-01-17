'''
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
'''

from pathlib import Path

__all__ = ['group_rename_files']


def group_rename_files(new_name: str, ext_renamed: str, /, count_dig: int = 3, ext_new: str = None,
                       saved_range: range = (3, 6), path: str = None) -> int:
    """Переименование файлов. Возвращает количество переименованных файлов.

    :new_name: Новое имя.
    :count_dig: Количество цифр в нумераторе.
    :ext_renamed: Расширение для переименования.
    :ext_new: Новое расширение. Если не указано - оставить исходное.
    :saved_range: Диапазон сохраняемых букв.
    :path: Каталог для обработки.
    """
    if ext_new is None:  # Сохранить расширение если не указано
        ext_new = ext_renamed
    # Рабочий каталог - текущий если не указан
    work_path = Path.cwd() if path is None else Path(path)
    count_renamed = 0
    for p in work_path.iterdir():
        if p.is_file() and p.suffix == ext_renamed:
            file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{count_renamed:03}{ext_new}"
            p.rename(Path(p.parent,  file_name))
            count_renamed += 1

    return count_renamed


if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_cnt = group_rename_files("_fn_", ".txt", path="./data_files")
    print(f"Переименовано: {files_cnt}")

'''
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''