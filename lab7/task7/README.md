# Задание №7 по варианту : `Шаблоны`

Студентка ИТМО,  Левчук Софья Александровна  466491

## Вариант 9

## Задание

Многие операционные системы используют шаблоны для ссылки на группы
объектов: файлов, пользователей, и т. д. Ваша задача – реализовать простейший
алгоритм проверки шаблонов для имен файлов.

В этой задаче алфавит состоит из маленьких букв английского алфавита и точки («.»). Шаблоны могут содержать произвольные символы алфавита, а также два
специальных символа: «?» и «*». Знак вопроса («?») соответствует ровно одному
произвольному символу. Звездочка «+» соответствует подстроке произвольной
длины (возможно, нулевой). Символы алфавита, встречающиеся в шаблоне, отображаются на ровно один такой же символ в проверяемой строчке. Строка считается
подходящей под шаблон, если символы шаблона можно последовательно отобразить на символы строки таким образом, как описано выше. Например, строчки
«ab», «aab» и «beda.» подходят под шаблон «*a?», а строчки «bebe», «а» и «ba»
–нет.
## Input / Output 

| Input            | Output |
|------------------|--------|
| k?t*n<br/>kitten | YES    |
| k?t?n<br/>kitten | NO     |


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
   cd Alg-Labs/lab7/task7
   ```
3. Запустите программу:
   ```bash
   python src/patterns.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    pytest tests/test_patterns.py
```