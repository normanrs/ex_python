def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) == len(strand_b):
      aList = list(strand_a)
      bList = list(strand_b)
      for idx, ltr in enumerate(aList):
        if (bList[idx] != ltr):
          count += 1
      return count
    else:
      raise ValueError("Strings are not the same length")