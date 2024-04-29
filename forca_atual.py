def forca(x):
  if x==0:
    print("------------")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==1:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==2:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==3:
    print("------------")
    print("|          |")
    print("|          0")
    print("|         -|")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==4:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|               ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==5:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         /      ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==6:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         / \\    ")
    print("|               ")
    print("|    Lamento! Perdeu! ")
    print("|")

erros=0
word=input('Informe a palavra: ');
temp=[]
for letra in word:
  temp.append('_')

while True:
  print('\n'*20)
  forca(erros)
  print('\n\nAdivinhe: ', end='')
  for let in temp:
    print(let, end=' ')
  print('\n'*2)

  if erros==6:
    break

  ganhouJogo=True
  for let in temp:
    if let=='_':
      ganhouJogo=False
  if ganhouJogo:
    print('\nPARABÉNS VENCEDOR!!!')
    break

  letraDig=input("Informe uma letra: ")

  errouLetra=True
  for i, let in enumerate(word):
    if word[i]==letraDig:
      temp[i]=word[i]
      errouLetra=False
  if errouLetra:
    erros=erros+1
