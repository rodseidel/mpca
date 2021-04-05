# Análise e Complexidade de Algoritmos

**Rodrigo Seidel**

**PPComp — Campus Serra, Ifes**

**2021-03**


## Breve explicação de como a técnica indicada foi utilizada
Após entrada dos dados necessários, organizando-se as opções selecionadas para cada dataset (pode ser informado mais de um), de acordo com a opção selecionada ('*' ou 'n' ou 'a b') são produzidas todas as combinações dos jornais indicados, de maneira ordenada e sem repetição.

A técnica de pesquisa completa foi utilizada na produção de todas as combinações dos jornais indicados, de acordo com a opção selecionada.


Foi recebido "Accepted" no Online Judge, conforme imagem a seguir (primeiro item da lista):

![Veredito](./00598-veredito.png)

## Análise da complexidade de tempo do programa desenvolvido
O ponto central desse programa é a produção das combinações possíveis. O número de combinações de n elementos combinados r vezes é dado pela fórmula Cnp = n!/( r!(n-r)! ).

Considerando o restante do programa e suas operações, elas não executarão um maior número de operações do que a produção das combinações possíveis de n elementos combinados em grupos de r.

Considerando também as opções de entrada ('*' ou 'n' ou 'a b') em qualquer um dos casos teremos que gerar todas as combinações de qualquer tamanho, formando-se o conjunto com todas as possibilidades de combinações. Sabe-se a quantidade de operações para se produzir esse conjunto é 2^n.

Portanto, a complexidade de tempo desse programa, desconsiderando as demais operações que são irrisórias frente a produção das combinações, será O(2^n).


https://wiki.python.org/moin/TimeComplexity

Apoio: 
https://justinbois.github.io/bootcamp/2020/lessons/l33_algorithmic_complexity.html
https://daemoniolabs.wordpress.com/tag/complexidade-combinacao



## Outras informações que o autor julgar apropriadas para o entendimento do trabalho realizado
Foi utilizada neste trabalho a biblioteca itertools, especificamente o método combinations (https://docs.python.org/3/library/itertools.html#itertools.combinations), através do qual se produz todas as combinações de elementos de uma lista, de maneira ordenada, sem repetição, de acordo com uma quantidade r informada.
