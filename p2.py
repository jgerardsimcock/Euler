def fibSeq(upperBoundary):
  return_value = 0

  for val in range(1, upperBoundary+1):
    if val % 2 == 0:
      return_value += val
      #print val
  print return_value

    #print return_value
    #return return_value 

fibSeq(4000000)
