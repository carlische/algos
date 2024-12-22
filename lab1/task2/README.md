# Задача 2: Сортировка вставками с отслеживанием индексов перемещения

## Описание

В данной задаче реализуется алгоритм сортировки вставками, который не только сортирует массив, но и отслеживает перемещения элементов. Алгоритм сортировки вставками проходит по элементам массива и вставляет каждый элемент в его правильную позицию среди уже отсортированных элементов. При этом алгоритм также возвращает список индексов, показывающий, как менялись позиции элементов в процессе сортировки.

### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (1 ≤ n ≤ 1000) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле output.txt должны содержаться две строки:
  1. Первая строка — индексы конечных позиций элементов после сортировки.
  2. Вторая строка — отсортированный массив. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab1/
|-- task2/
|   |-- input.txt                  # Входные данные
|   |-- sort2.py                   # Реализация алгоритма сортировки вставками с отслеживанием индексов
|   |-- output.txt                 # Выходные данные
|   |-- test_insertion_sort_with_indices.py # Тесты для проверки корректности работы алгоритма
```
## Код задачи
```
def insertion_sort(arr):
    index = [0]
    counter = 0
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = j, i
        counter += 1
        index.append(counter)
    return index, arr

if __name__ == '__main__':
    with open('input.txt') as f:
        n, array_1 = f.readlines()
    indexes, array_2 = insertion_sort(list(map(int, array_1.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, indexes))), file=f)
        print(' '.join(list(map(str, array_2))), file=f)
```
## Запуск проекта

1. Перейдите в директорию task2.
2. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
3. Запустите скрипт:
      python sort2.py
   
4. Результат выполнения будет записан в файл output.txt.

## Тестирование

Для проверки корректности работы программы выполните тесты, находящиеся в директории task2.

1. Выполните команду:
      python -m unittest test_insertion_sort_with_indices.py
   

### Тесты
```
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sort2 import insertion_sort

class TestInsertionSortWithIndices(unittest.TestCase):
    """
    Набор тестов для функции сортировки вставками с отслеживанием перемещений элементов.
    """

    def test_basic_case(self):
        """
        Проверка корректной сортировки и возвращаемых индексов при обычном случае.
        """
        indexes, sorted_array = insertion_sort([4, 3, 2, 1])
        self.assertEqual(sorted_array, [1, 2, 3, 4])
        self.assertEqual(indexes, [0, 1, 2, 3])

    def test_with_duplicates(self):
        """
        Проверка корректной сортировки и возвращаемых индексов при наличии дубликатов в массиве.
        """
        indexes, sorted_array = insertion_sort([3, 3, 1, 2, 3])
        self.assertEqual(sorted_array, [1, 2, 3, 3, 3])
        self.assertEqual(indexes, [0, 1, 2, 3, 4])

    def test_sorted_array(self):
        """
        Проверка корректности работы на уже отсортированном массиве.
        """
        indexes, sorted_array = insertion_sort([1, 2, 3, 4, 5])
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        self.assertEqual(indexes, [0, 1, 2, 3, 4])

    def test_single_element(self):
        """
        Проверка корректности работы на массиве с одним элементом.
        """
        indexes, sorted_array = insertion_sort([42])
        self.assertEqual(sorted_array, [42])
        self.assertEqual(indexes, [0])

    def test_empty_array(self):
        """
        Проверка работы на пустом массиве.
        """
        indexes, sorted_array = insertion_sort([])
        self.assertEqual(sorted_array, [])
        self.assertEqual(indexes, [0])

if __name__ == '__main__':
    unittest.main()
```
## Пример

### Входные данные (input.txt)
4
4 3 2 1

### Выходные данные (output.txt)
0 1 2 3
1 2 3 4
