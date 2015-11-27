def sumThreeFive(number):
  count = 0
  for val in range(1, number):
    if (val % 3 == 0) or (val % 5 == 0):
      count += val
  print count
  return count


sumThreeFive(1000)