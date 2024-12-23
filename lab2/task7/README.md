# Задание 7: Поиск максимального подмассива за линейное время
Студентка ИТМО,  Левчук Софья Александровна  466491

## Описание
Можно найти максимальный подмассив за линейное время, воспользовавшись следующими идеями. Начните с левого конца массива и двигайтесь вправо, отслеживая найденный к данному моменту максимальный подмассив. Зная максимальный подмассив массива A[1..j], распространите ответ на поиск максимального подмассива, заканчивающегося индексом j + 1, воспользовавшись следующим наблюдением: максимальный подмассив массива A[1..j + 1] представляет собой либо максимальный подмассив массива A[1..j], либо подмассив A[i..j + 1] для некоторого 1 ≤ i ≤ j + 1. Определите максимальный подмассив вида A[i..j + 1] за константное время, зная максимальный подмассив, заканчивающийся индексом j. 

## Структура проекта

```
Task-7/
|-- src/
|   |-- input.txt
|   |-- m_suberray.py
|   |-- output.txt
|-- tests/
|   |-- test_m_suberray.py
```

## Ограничения по времени и памяти

- Ограничение по времени: 2 сек.
- Ограничение по памяти: 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SofyaLev/Alg-Labs.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Alg-Labs/lab2/task7
   ```
3. Запустите программу:
   ```bash
   python src/find_max_subarray.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    pytest tests/test_find_max_subarray.py
```
