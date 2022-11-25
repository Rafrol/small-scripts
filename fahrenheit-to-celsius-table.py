def to_celsius(x):
  return (x-32)*5/9
for x in range (0,131,5):
  print(str(x) + "degrees in Fahrenheit is the same as " + str(to_celsius(x)) + " degrees in Celsius")
