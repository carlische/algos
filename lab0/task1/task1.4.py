with open('input.txt','r') as f:
  a,b = map(int, f.readline().split())
f.close()

if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
  with open('output.txt', 'w') as f:
      f.write(str(a + b*b))
  f.close()
else:
  print('Numbers are out of range')