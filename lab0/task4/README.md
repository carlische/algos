# Задача 4: Тестирование ваших алгоритмов

## Описание
Необходимо протестировать время выполненичя вашего алгоритма в Задании 2 и Задании 3.

## Код задач
1. Задача 2
```
import time
t_start = time.perf_counter()
def calc_fib(n): if n <= 1:
      return n
  else:
s = [0, 1]
for i in range(2, n+1):
s.append(s[i-1] + s[i-2]) return s[n]
with open('input.txt', 'r') as f: n = int(f.readline())
f.close()
if 0 <= n <= 45:
a = calc_fib(n)
with open('output.txt', 'w') as f:
f.write(str(a)) f.close()
else:
print('Numbers are out of range')
print(time.perf_counter() - t_start)
```
2. Задача 3
```
import time
t_start = time.perf_counter()
def calc_fib(n): if n <= 1:
return n
else:
s1, s2 = 0, 1
for i in range(2, n+1):
s1, s2 = s2, (s1 + s2) % 10
return s2
with open('input.txt', 'r') as f: n = int(f.readline())
f.close()
if 0 <= n <= 10**7:
a = calc_fib(n)
with open('output.txt', 'w') as f:
f.write(str(a)) print(time.perf_counter() - t_start)
```
