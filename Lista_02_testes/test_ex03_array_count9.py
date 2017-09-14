# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# C. array_count9
# conta quantas vezes aparece o 9 numa lista nums
def array_count9(nums):
  cont = 0
  num=0
  for e in nums:
    if e == 9:
      cont +=1
      print(cont)
  return cont

def test_ex03():
  print ('Array count 9')
  assert array_count9([1, 99, 9]) == 1
  assert array_count9([1, 9, 9]) == 2
  assert array_count9([1, 9, 9, 3, 9]) == 3
  assert array_count9([1, 2, 3]) == 0
  assert array_count9([]) == 0
  assert array_count9([4, 2, 4, 3, 1]) == 0
  assert array_count9([9, 2, 99, 3, 1]) == 1


