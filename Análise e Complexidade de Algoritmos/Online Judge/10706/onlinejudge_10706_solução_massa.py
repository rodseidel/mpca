t = 0
while t < 1 or t > 25:
  t = int(input())

posicoes_a_pesquisar = []

for p in range(t):
  posicoes_a_pesquisar.append(int(input()))


for s in range(len(posicoes_a_pesquisar)):
  i = posicoes_a_pesquisar[s]

  temp = 0
  move = 0
  cnt = 0
  dig = 0

  while (move < i):
    cnt += 1
    temp = cnt
    while (temp != 0):
      dig += 1
      temp = temp // 10     #C /= A is equivalent to C = C / A
    move = move + dig

  temp = cnt

  while (move != i):
    move -= 1
    temp = temp//10
    if (temp == 0):
      cnt -= 1
      temp = cnt

  print(str(temp % 10))



