cases = int(input(''))
while cases:
  number = int(input(''))
  cases -= 1
  first = False if number<=1 else True
  for i in range(2, number):
    if number % i == 0:
      first = False
  if first:
    print("Liczba jest pierwsza")
  else:
    print("Liczba NIE JEST pierwsza")
