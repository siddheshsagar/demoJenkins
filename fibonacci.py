# This is a simple program to find Fibonacci series up to n

import random

lis = [i for i in range(2,21)]
n = random.choice(lis)

fibo_sequence = [0 for i in range(n)]
fibo_sequence[1] = 1
for i in range(2,n):
  fibo_sequence[i] = fibo_sequence[i-1]+fibo_sequence[i-2]
print(fibo_sequence)
  



