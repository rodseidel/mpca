# Análise e Complexidade de Algoritmos

Rodrigo Seidel

PPComp — Campus Serra, Ifes

2020-03


## Breve explicação de como a técnica indicada foi utilizada
Após entrada dos dados necessários, organizando-se as opções selecionadas para cada dataset (pode ser informado mais de um), de acordo com a opção selecionada ('*', 'n' ou 'a b') são produzidas todas as combinações dos jornais indicados, de maneira ordenada e sem repetição.

A técnica de pesquisa completa foi utilizada na produção de todas as combinações dos jornais indicados, de acordo com a opção selecionada.


Foi recebido "Accepted" no Online Judge, conforme imagem a seguir (primeiro item da lista):

![Veredito](./00598-veredito.png)

## Análise da complexidade de tempo do programa desenvolvido



## Outras informações que o autor julgar apropriadas para o entendimento do trabalho realizado
Foi utilizada neste trabalho a biblioteca itertools, especificamente o método combinations (https://docs.python.org/3/library/itertools.html#itertools.combinations), através do qual se produz todas as combinações de elementos de uma lista, de maneira ordenada, sem repetição, de acordo com uma quantidade r informada.
