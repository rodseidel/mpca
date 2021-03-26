from itertools import combinations
#https://docs.python.org/3/library/itertools.html#itertools.combinations

def combinacao(jornais,num_posicoes):
  comb = []
  for p in combinations(jornais, r=num_posicoes):
    comb.append(p)
  return comb

while True:
  try:
    qtd_datasets = int(input())
    input()

    regra_formacao_resultado = input()
    
    jornais = []
    jornal = "-"

    i = 0
    while i < 12:
      
      jornal = input()
      if jornal == "":
        break
    
      jornais.append(jornal)
      i += 1

    
    regras = regra_formacao_resultado.split(" ")

    if len(regras) == 1:
    
      if regras[0] == "*":
        #"*" significa mostrar todos os tamanhos de subconjunto de 1 ao número de jornais na lista
        for i in range(len(jornais)):
          print("Size " + str(i+1))
          
          combina = combinacao(jornais,i+1)
          
          for j in range(len(combina)):
            print(','.join(combina[j]).replace(",",", "))

          print("")
       

      else:  
        #"n" significa mostrar apenas subconjuntos de tamanho n
        print("Size " + str(regras[0]))
        
        combina = combinacao(jornais,int(regras[0]))
        
        for j in range(len(combina)):
          print(','.join(combina[j]).replace(",",", "))
        
        print("")
    
    
    elif len(regras) == 2:
      #"a b" significa mostrar todos os tamanhos de subconjunto de a a b, inclusive
      for i in range(int(regras[0]),int(regras[1])+1):
        
        print("Size " + str(i))
        
        combina = combinacao(jornais,i)
        
        for j in range(len(combina)):
          print(','.join(combina[j]).replace(",",", "))
        
        print("")

  except EOFError:
    break

