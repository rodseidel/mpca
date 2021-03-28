import math

n=65536 #65536 #chegamos ao maior valor acumulado de 2147516416, que contempla o maior i

#Fórmula para identificar a quantidade de dígitos de determinado número = int(math.log(x)+1)
# 96 = 2
# 115 = 3

qtd_algarismos_grupo = {1:1};
historicoCalculos = {1:1};

for i in range(2,n):
  #cache para calculo da quantidade de algarismos de um grupo, considerando o cálculo feito para o grupo anterior
  qtd_algarismos_grupo[i] = qtd_algarismos_grupo.get(i-1) + int(math.log10(i)+1) 
  
  #cache para armazenar a total acumulado de quantidades do grupo, considerando o cálculo feito para o grupo anteiror
  historicoCalculos[i] = historicoCalculos.get(i-1) + qtd_algarismos_grupo.get(i)

t = 0
while t < 1 or t > 25:
  t = int(input())

posicoes_a_pesquisar = []

for p in range(t):
  posicoes_a_pesquisar.append(int(input()))


for s in range(len(posicoes_a_pesquisar)):
  i = posicoes_a_pesquisar[s]
  
  indice_a_expandir = 0
  #Como o histórico de calculos está organizado, faz uma busca simples com for, buscando posição em que o total alcumulado da quantidade de algarismos do grupo ultrapassa ou é igual a quantidade 'i' buscada
  #É nesse conjunto que deverá ser feita a busca linear para identificação do algarismo na posição i
  for a in range(len(historicoCalculos)):
    if historicoCalculos.get(a+1) >= i:
      indice_a_expandir = a+1
      break
  
  #expande sequencia numerica da posição localizada, para busca linear
  sequencia_numerica = []
  for k in range(indice_a_expandir):
    sequencia_numerica.append(str(k+1))
    
  sequencia_numerica = ''.join(sequencia_numerica)
  
  #identifica o valor acumulado da quantidade de algarismos até o fim da posição anterior
  pos_inicial = historicoCalculos.get(indice_a_expandir-1)

  #o caracter a ser retornado é o que se encontra na posição que é a diferença entre o 'i' e o somatório acumulado da posição anterior
  print(sequencia_numerica[:(i - pos_inicial)][-1])


