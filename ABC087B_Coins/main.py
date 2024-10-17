# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())

a=60
b=50
c=40
x=6000

x = int(x/50)

def max(a,b):
  return a if a > b else b

def min(a,b):
  return a if a < b else b

a_0 = min(a,x//10)

def cases_rem(n,b,c):
  parity = n%2
  n -= parity
  c -= parity
  if (2*b+c)<n or c<0:
    return 0
  return min(n//2,b)-max((n-c)//2,0)+1

cases = 0

for i in range(0,min(a,x//10)+1):
  cases += cases_rem(x-10*i,b,c)


print(cases)