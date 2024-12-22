# Задача 1: Сортировка вставками

## Описание

В данной задаче реализуется алгоритм сортировки вставками. Алгоритм работает путём последовательного прохода по элементам массива и вставки каждого элемента в его правильную позицию среди уже отсортированных элементов. Такой подход позволяет сортировать массив с минимальным использованием дополнительной памяти.

### Формат входных данных
- Входные данные находятся в файле input.txt.
- Первая строка содержит одно число n (1 ≤ n ≤ 1000) — количество элементов в массиве.
- Вторая строка содержит n целых чисел, по модулю не превосходящих 10^9.

### Формат выходных данных
- В выходном файле output.txt должен содержаться отсортированный массив. Все числа должны быть разделены ровно одним пробелом.

### Ограничения
- Время выполнения: 2 секунды.
- Память: 256 МБ.

## Структура проекта
```
lab1/
|-- task1/
|   |-- input.txt          # Входные данные
|   |-- sort1.py           # Реализация алгоритма сортировки вставками
|   |-- output.txt         # Выходные данные
|   |-- test_insertion_sort.py # Тесты для проверки корректности работы алгоритма
```
## Код задачи
```
def insertion_sort(arr):
    for i in range(1, len(arr)):
        arg = arr[i]
        j = i - 1
        while j >= 0 and arg < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arg
    return arr

if __name__ == '__main__':
    with open('input.txt') as f:
        n, array_1 = f.readlines()
    array_2 = insertion_sort(list(map(int, array_1.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array_2))), file=f)
```
## Запуск проекта

1. Перейдите в директорию task1.
2. Убедитесь, что файл input.txt содержит корректные входные данные в указанном формате.
3. Запустите скрипт:
      python sort1.py
   
4. Результат выполнения будет записан в файл output.txt.

## Тестирование

Для проверки корректности работы программы выполните тесты, находящиеся в директории task1.

1. Выполните команду:
      python -m unittest test_insertion_sort.py
   

### Тесты
```
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from sort1 import insertion_sort

class TestInsertionSort(unittest.TestCase):
    """
    Набор тестов для функции сортировки вставками.
    """

    def test_sorted_array(self):
        """
        Проверка работы на уже отсортированном массиве.
        """
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """
        Проверка работы на массиве, отсортированном в обратном порядке.
        """
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        """
        Проверка работы на случайном неотсортированном массиве.
        """
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

    def test_array_with_duplicates(self):
        """
        Проверка работы на массиве с дубликатами.
        """
        self.assertEqual(insertion_sort([2, 3, 2, 3, 1]), [1, 2, 2, 3, 3])

    def test_single_element_array(self):
        """
        Проверка работы на массиве с одним элементом.
        """
        self.assertEqual(insertion_sort([42]), [42])

    def test_empty_array(self):
        """
        Проверка работы на пустом массиве.
        """
        self.assertEqual(insertion_sort([]), [])

if __name__ == '__main__':
    unittest.main()
```
## Пример

### Входные данные (input.txt)
6
31 41 59 26 41 58

### Выходные данные (output.txt)
26 31 41 41 58 59
