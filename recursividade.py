print("#####################################")
print("########### RECURSIVIDADE ##########")
print("##### AUTOR TIMMERS A. ##########")
print("############# 1 QUEST #############")

def exp(num: int, expo: int) -> int:
  if expo == 0:
    return 1
  return num * exp(num, expo - 1)

print('5^4=', exp(5, 5))

print("############# 2 QUEST #############")

def mult(primFat: int, segFator: int) -> int:
  if primFat == 0:
    return 0
  return segFator + mult(primFat - 1, segFator)

print('5x7=', mult(5, 9))

print("############# 3 QUEST #############")

def fib(index: int):
  if index == 0:
    return 0
  elif index == 1:
    return 1
  return fib(index - 1) + fib(index - 2)

print('f(8)=', fib(8))
