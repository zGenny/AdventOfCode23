result = 0 
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
with open("./input2.txt","r") as f:
  for riga in f.readlines():
    riga = riga.replace('Game ','')
    riga = riga.replace('\n','')
    riga = riga.replace(':','')
    riga = riga.replace(',','')
    riga = riga.replace(';','')
    rigaListed = riga.split(' ')
    
    maxRed = 0 
    maxGreen = 0
    maxBlue = 0
    
    for i in range(0,len(rigaListed),2):
      if i==0:
        continue
      else:
        if rigaListed[i] == 'red':
          if int(rigaListed[i-1]) > maxRed:
            maxRed = int(rigaListed[i-1])
            print('red: ',maxRed)
        if rigaListed[i] == 'green':
          if int(rigaListed[i-1]) > maxGreen:
            maxGreen = int(rigaListed[i-1])
        if rigaListed[i] == 'blue':
          if int(rigaListed[i-1]) > maxBlue:
            maxBlue = int(rigaListed[i-1])
    result += maxRed * maxGreen * maxBlue
    print(result)