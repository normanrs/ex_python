def raindrops(number):
    drop = []
    if (number % 3 == 0):
      drop.append("Pling")
    if (number % 5 == 0):
      drop.append('Plang') 
    if (number % 7 == 0):
      drop.append('Plong') 
    if drop:
      return ''.join(drop)
    else:
      return str(number)
