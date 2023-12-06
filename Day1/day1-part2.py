somma = 0

listaNumeri = []

for i in range(10):
  listaNumeri.append(str(i))

NumeriLettere    = ["one","two","three","four","five","six","seven","eight","nine"]

# two1nine
# eightwothree
# abcone2threexyz
#
#
#



def traduciRiga(riga):
  stringa = ""
  for i in range(len(riga)):
    if riga[i] in listaNumeri:
      stringa += riga[i]
    else:
      for j in range(5):
        if riga[i:i+j+1] in NumeriLettere:
          stringa += str(NumeriLettere.index(riga[i:i+j+1])+1)
          break
  
  return stringa

def trovaNumero(riga):
  return riga[0]

with open("inputDay1-part2.txt",'r') as f1:
  while True:
    riga1 = f1.readline()
    riga1 = traduciRiga(riga1)
    print(riga1)
    riga2 = riga1[::-1]
    if not riga1:
      break
    num = trovaNumero(riga1)+trovaNumero(riga2)
    print(num)
    somma += int(num)
print(somma)