casos_teste = []

numero_testes = int(input())

#INPUT
for i in range(numero_testes):
  
  #o número de tipos de moedas não será armazenado pois é possível
  # identificar ao buscar o len da lista da próxima entrada
  input()
  
  lista_valores = []
  valores = input().split()

  for v in range(len(valores)):
    lista_valores.append(int(valores[v]))
    
  casos_teste.append(lista_valores)

#  withdraw (X) {
#     if (X == 0) return;
#     Let Y the highest valued coin that does not exceed X.
#     Give the customer Y valued coin.
#     withdraw (X-Y);
#  }

#PROCESSAMENTO
for ct in range(len(casos_teste)):
  
  # a soma não deve ultrapassar a próxima moeda maior, caso contrário, produzirá o pior resultado
  # inclui as menores moedas sem ultrapassar o valor da próxima moeda
  
  valores = casos_teste[ct]
  qtdTiposMoedas = 0 
  somaValores = 0
  

  for v in range(len(valores)):
    #A primeira e última moedas sempre serão consideradas pois:
    # qualquer valor a sacar maior que o maior valor fará a retirada da maior moeda.
    # qualquer valor igual ao menor valor fará a retirada da menor moeda
    #Nas intermediárias, se a moeda seguinta tiver maior valor que a soma dos valores até o momento mais o valor da moeda atual, conta aquela moeda e acumula no valor.
    #O contador final será acrescido de +1 para atender o caso de 1 moeda apenas na lista e considerar a última moeda
    if v+1 != len(valores):
      if valores[v+1] > somaValores + valores[v]:
        somaValores += valores[v]
        qtdTiposMoedas += 1
  
  print(qtdTiposMoedas+1)

