# ASSIGNMENT 1_PART 01

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def listDivide(numbers, divide = 2):
  """
  This function returns the number of elements in the numbers list that are divisible by divide.

  Args: 
    numbers (list): The list of numbers to be checked
    divide (int): The number to divide the elements in the list by

  Return:
    divisible count: Count of elements in the list that are divisible by divide
  """
  divisible_count = 0

  for i in numbers:
    if i % divide == 0:
      divisible_count += 1
  return divisible_count


class ListDivideException(Exception):
  pass


def testListDivide():
  """
  This function tests the listDivide function.
  """
  assert listDivide([1,2,3,4,5]) == 2
  assert listDivide([2,4,6,8,10]) == 5
  assert listDivide([30, 54, 63,98, 100], divide = 10) == 2
  assert listDivide([]) == 0
  assert listDivide([1,2,3,4,5], 1) == 5

if __name__ == "__main__":
  testListDivide()