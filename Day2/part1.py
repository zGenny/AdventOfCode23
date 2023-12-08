result = 0 
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
with open("./input1.txt","r") as f:
  for riga in f.readlines():
    print(riga)
    riga = riga.replace('Game ','')
    riga = riga.replace('\n','')
    riga = riga.replace(':','')
    riga = riga.replace(',','')
    riga = riga.replace(';','')
    rigaListed = riga.split(' ')
    
    for i in range(0,len(rigaListed),2):
      if i==0:
        result += int(rigaListed[0])
      else:
        if rigaListed[i] == 'red':
          if int(rigaListed[i-1]) > MAX_RED:
            result -= int(rigaListed[0])
            break
        elif rigaListed[i] == 'green':
          if int(rigaListed[i-1]) > MAX_GREEN:
            result -= int(rigaListed[0])
            break
        elif rigaListed[i] == 'blue':
          if int(rigaListed[i-1]) > MAX_BLUE:
            result -= int(rigaListed[0])
            break
    print(result)