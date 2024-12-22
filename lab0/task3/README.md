# Задача 3: Ещё про числа Фибоначчи

## Описание
Разработать алгоритм для подсчета последней цифры числа Фибоначчи.

## Код задачи
```
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
```
