#INPUT
testes = []
teste = []

input_testes_finalizado = False

while not input_testes_finalizado:

  altura = int(input())
  
  if altura == -1 and len(teste) == 0:
    input_testes_finalizado = True
  
  elif altura == -1:
    
    testes.append(teste.copy())
    teste.clear()
  
  else:
  
    teste.append(altura)

#PROCESSAMENTO
#O míssil que se aproxima é o primeiro míssil a ser interceptado neste teste. OU
#O míssil foi disparado após o último míssil interceptado e NÃO ESTÁ MAIS ALTO do que o último míssil interceptado.

for t in range(len(testes)):
  
  altura_anterior_interceptado = -1
  qtd_missil_interceptado = 0

  for m in range(len(testes[t])):
    
    altura_missil_atual = testes[t][m]

    if altura_anterior_interceptado == -1 or altura_anterior_interceptado >= altura_missil_atual:
      qtd_missil_interceptado += 1
      altura_anterior_interceptado = altura_missil_atual
    
  print("Test #{}:".format(t+1))
  print("  maximum possible interceptions: {}\n".format(qtd_missil_interceptado))

