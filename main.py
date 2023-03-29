"""
Напишіть Python-скрипт, який зчитує вміст двох файлів з розширенням ".txt",
порівнює їх та записує у файл з назвою "same.txt" всі рядки, які містяться в обох файлах,
у файл "diff.txt" - рядки, які містяться лише в одному з двох файлів.
"""

import os

# Вказуємо теку з файлами
folder_path = "files"

# Створюємо порожні списки для збереження рядків з файлів
file1_lines = []
file2_lines = []

# Зчитуємо файли з теки з розширенням .txt
for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        with open(os.path.join(folder_path, file_name), "r") as f:
            if file_name == "file_1.txt":
                file1_lines = f.readlines()
            elif file_name == "file_2.txt":
                file2_lines = f.readlines()
