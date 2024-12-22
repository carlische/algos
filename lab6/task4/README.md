# Задание №4 по выбору  : `Прошитый ассоциативный массив`

Студентка ИТМО,  Левчук Софья Александровна  466491

## Вариант 9

## Задание 
Реализуйте прошитый ассоциативный массив. Ваш алгоритм должен поддерживать следующие типы операций:

• get x – если ключ x есть в множестве, выведите соответствующее ему
значение, если нет, то выведите <none>.

• prev x – вывести значение, соответствующее ключу, находящемуся в ассоциативном массиве, который был вставлен позже всех, но до x, или <none>,
если такого нет или в массиве нет x.

• next x – вывести значение, соответствующее ключу, находящемуся в ассоциативном массиве, который был вставлен раньше всех, но после x , или
<none>, если такого нет или в массиве нет x.

• put x y – поставить в соответствие ключу x значение y. При этом следует
учесть, что
   
– если, независимо от предыстории, этого ключа на момент вставки в
массиве не было, то он считается только что вставленным и оказывается самым последним среди добавленных элементов – то есть, вызов
next с этим же ключом сразу после выполнения текущей операции put
должен вернуть <none>;
   
– если этот ключ уже есть в массиве, то значение необходимо изменить,
и в этом случае ключ не считается вставленным еще раз, то есть, не
меняет своего положения в порядке добавленных элементов.

• delete x – удалить ключ x. Если ключа в ассоциативном массиве нет, то
ничего делать не надо.

## Input / Output 

| Input                                                                                                                                                                                            | Output                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| put zero a<br/>put one b<br/>put two c <br/>put three d<br/>put four e<br/>get two<br/>prev two<br/>next two<br/>delete one<br/>delete three<br/>get two<br/>prev two<br/>next two<br/>next four | c<br/>b<br/>d<br/>c<br/>a<br/>e<br/> none |


## Ограничения по времени и памяти

- Ограничение по времени: 4 сек.
- Ограничение по памяти: 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SofyaLev/Alg-Labs.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd Alg-Labs/lab6/task4
   ```
3. Запустите программу:
   ```bash
   python src/associative_massive.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    pytest tests/test_associative_massive.py
```