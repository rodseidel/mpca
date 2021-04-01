casos_teste = []
eventos = []
###############
# posição 0 - tipo
# posicao 1 - distancia do início
# posicao 2 - consumo combustível
###############

#ENTRADA DOS DADOS
while True:
  entrada = input().split(" ")

  if entrada[1] == "Fuel" and entrada[3] == "0":
    break
  
  else:

    if len(entrada) == 4:
      distancia_inicio = entrada[0]
      tipo = "".join(entrada[1] + " " + entrada[2])
      consumo = entrada[3]
    else:
      distancia_inicio = entrada[0]
      tipo = entrada[1]
      consumo = 0

  eventos.append((tipo,distancia_inicio,consumo))
  #print("Tipo: {} / distancia: {} / consumo: {}".format(tipo,distancia_inicio, consumo))
  #print("Eventos {}".format(eventos))

  if tipo == "Goal":
    casos_teste.append(eventos.copy())
    eventos.clear()
    #print("Casos teste {}".format(casos_teste))
    #print("--")

def maior(a,b):
  if a > b:
    return a
  
  return b

#PROCESSAMENTO
###############
# posição 0 - tipo
# posicao 1 - distancia do início
# posicao 2 - consumo combustível
###############

for ct in range(len(casos_teste)):
  
  eventos = casos_teste[ct]
  #print("caso" + str(ct+1)) 
  
  menor_consumo_possivel = float(0)
  consumo = float(eventos[0][2])
  distancia_inicio = 0
  furo = float(0)
  ultimo_furo = int(0)
  consumo_atual = float(0)

  #Processa eventos do caso de teste
  for ev in range(len(eventos)):
    
    #print(eventos[ev])
    #print("  >>>> ANTES")
    #print("menor_consumo_possivel {}".format(menor_consumo_possivel))
    #print("consumo {}".format(consumo))
    #print("distancia_inicio {}".format(distancia_inicio))
    #print("furo {}".format(furo))
    #print("ultimo_furo {}".format(ultimo_furo))
    #print("consumo_atual {}".format(consumo_atual))
    #print("")

    distancia_evento = int(eventos[ev][1])
    #print("  >>>> DEPOIS")

    consumo_atual += (consumo*(distancia_evento-distancia_inicio))/100;
    #print("  consumo_atual {}".format(consumo_atual))
    
    consumo_atual += (furo*(distancia_evento-ultimo_furo));
    #print("  consumo_atual {}".format(consumo_atual))

    menor_consumo_possivel = maior(menor_consumo_possivel, consumo_atual);
    distancia_inicio = distancia_evento
    ultimo_furo = distancia_evento;
    
    #print("menor_consumo_possivel {}".format(menor_consumo_possivel))
    #print("consumo {}".format(consumo))
    #print("distancia_inicio {}".format(distancia_inicio))
    #print("furo {}".format(furo))
    #print("ultimo_furo {}".format(ultimo_furo))
    #print("consumo_atual {}".format(consumo_atual))
    #print("----------------------------------------------")


    if eventos[ev][0] == "Fuel consumption":   #Consumo de combustível x litros a cada 100 km
       consumo = float(eventos[ev][2])

    elif eventos[ev][0] == "Leak":      #Tanque furado, perde 1 litro de combustível por quilometro
        furo += 1

    elif eventos[ev][0] == "Gas":       #Enche o tanque
        consumo_atual = 0

    elif eventos[ev][0] == "Mechanic":  #Conserta o furo no tanque
        furo = 0

    elif eventos[ev][0] == "Goal":      #Fim do trajeto
        print(format(menor_consumo_possivel,'.3f'))
