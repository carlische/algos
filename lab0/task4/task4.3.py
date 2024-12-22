import time
t_start = time.perf_counter()

def calc_fib(n):
  if n <= 1:
      return n
  else:
      s1, s2 = 0, 1
      for i in range(2, n+1):
          s1, s2 = s2, (s1 + s2) % 10
      return s2

with open('input.txt', 'r') as f:
  n = int(f.readline())
f.close()

if 0 <= n <= 10**7:
  a = calc_fib(n)
  with open('output.txt', 'w') as f:
      f.write(str(a))

print(time.perf_counter() - t_start)