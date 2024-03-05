"""Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт,
который вы запускаете:"""

import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
print(os.path.abspath(__file__))  # Путь + имя файла
print(os.path.abspath(os.path.dirname(__file__)))  # Только путь

"""Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file". Мы должны сначала найти 
этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path)."""
