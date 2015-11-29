def fibSeq(upperBoundary):
  fib = 1
  fib2 = 2
  temp = 0
  total = 0

  while temp <= upperBoundary:
      temp = fib2
      if not temp % 2:
        total += temp

      fib, fib2 = fib2, fib + fib2

  print total


fibSeq(4000000)


def even_fib(limit):
  a, b = 0, 1
  while a < limit:
    if not a % 2:
        yield a

    a, b = b, a + b

#print sum(even_fib(4000000))