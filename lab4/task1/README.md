# Задание №1 по варианту  : `Стек`

Студентка ИТМО,  Левчук Софья Александровна  466491

## Вариант 9

## Задание 
Реализуйте работу стека. Для каждой операции изъятия элемента выведите ее
результат.

На вход программе подаются строки, содержащие команды. Каждая строка содержит одну команду. Команда — это либо “+ N”, либо “–”. Команда “+ N”означает добавление в стек числа N, по модулю не превышающего 10^9. Команда “–” означает изъятие элемента из стека. Гарантируется, что не происходит
извлечения из пустого стека. Гарантируется, что размер стека в процессе выполнения команд не превысит 10^6 элементов.
 
## Input / Output 

| Input                                       | Output      |
|---------------------------------------------|-------------|
| + 1<br/>+ 10<br/>-<br/>+ 2<br/>+ 1234<br/>- | 10<br/>1234 |


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
   cd Alg-Labs/lab4/task1
   ```
3. Запустите программу:
   ```bash
   python src/stack.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    pytest tests/test_Stack.py
```