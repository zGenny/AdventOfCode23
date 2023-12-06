somma = 0

listaNumeri = []

for i in range(10):
  listaNumeri.append(str(i))

def trovaNumero(riga):
  for c in riga:
    if c in listaNumeri:
      return c
  return None

with open("inputDay1-part1.txt",'r') as f1:
  while True:
    riga1 = f1.readline()
    riga2 = riga1[::-1]
    if not riga1:
      break
    num = trovaNumero(riga1)+trovaNumero(riga2)
    somma += int(num)
print(somma)