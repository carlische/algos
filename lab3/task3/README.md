# Задание №3 по выбору : `Сортировка пугалом`

Студентка ИТМО,  Левчук Софья Александровна  466491

## Вариант 9

## Задание 
«Сортировка пугалом» — это давно забытая народная потешка. Участнику под верхнюю одежду продевают деревянную палку, так что у него оказываются растопырены руки, как у огородного пугала. Перед ним ставятся n матрёшек в ряд. Из-за палки единственное, что он может сделать — это взять в руки две матрешки на расстоянии k друг от друга (то есть i-ую и i + k-ую), развернуться и поставить их обратно в ряд, таким образом поменяв их местами. 

Задача участника — расположить матрёшки по неубыванию размера. Может ли он это сделать?

## Input / Output 

| Input              | Output |
|--------------------|--------|
| 3 2<br/> 2 1 3     | NO     |
| 5 3<br/> 1 5 3 4 1 | YES    |

## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SofyaLev/Alg-Labs.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Alg-Labs/lab3/task3
   ```
3. Запустите программу:
   ```bash
   python src/scarecrow_sort.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    pytest tests/test_scarecrow_sort.py
```