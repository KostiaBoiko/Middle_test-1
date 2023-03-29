"""
Напишіть Python-скрипт, який зчитує вміст двох файлів з розширенням ".txt",
порівнює їх та записує у файл з назвою "same.txt" всі рядки, які містяться в обох файлах,
у файл "diff.txt" - рядки, які містяться лише в одному з двох файлів.
"""

import os

class Loader:
    def __init__(self):
        # Вказуємо теку з файлами
        self.folder_path = "files"


    # Зчитуємо файли з теки з розширенням .txt
    def read_files(self):
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".txt"):
                with open(os.path.join(self.folder_path, file_name), "r") as f:
                    if file_name == "file_1.txt":
                        file1_lines = f.readlines()
                    elif file_name == "file_2.txt":
                        file2_lines = f.readlines()
        return file1_lines, file2_lines


    # Знаходимо рядки, які містяться в обох файлах
    def write_same_lines(self, file1, file2):
        same_lines = set(file1).intersection(file2)
        return same_lines



