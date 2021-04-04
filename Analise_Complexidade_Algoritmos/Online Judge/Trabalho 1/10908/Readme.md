# Análise e Complexidade de Algoritmos

**Rodrigo Seidel**

**PPComp — Campus Serra, Ifes**

**2021-03**

## Breve explicação de como a técnica indicada foi utilizada
Após entrada dos dados necessários é feita uma verificação do tamanho do grid informado, pois dependendo da forma do grid, o maior tamanho possível do quadrado sempre será 1, independente da coordenada pesquisada.

Também me utilizei da característica do problema de que o lado do quadrado sempre será ímpar, descartando pesquisas de lados pares.

A partir daí foi necessário apenas fazer a pesquisa em torno da coordenada informada, sempre fazendo isso em camadas e sempre conferindo se todos os elementos da camada são iguais ao da coordenada buscada.

Caso na camada exista algum caracter diferente do buscado ou caso a coordenada caia em uma região fora do grid, a camada é rejeitada.

A técnica de pesquisa completa foi utilizada de forma que para confirmar o maior lado do quadrado possível a partir de uma coordenada, todas as outras coordenadas em torno dela são geradas e verificadas, sempre respeitando as camadas e o tamanho do grid.


Foi recebido "Accepted" no Online Judge, conforme imagem a seguir (primeiro item da lista):

![Veredito](./10908-veredito.png)

## Análise da complexidade de tempo do programa desenvolvido

Número de testes: T
Número de Localizações: L
Número de tamanhos de lados: f
Número de coordenadas X: n
Número de coordenadas Y: n

Foram desconsiderados custos irrelevantes, como atribuição de váriáveis, append em listas, etc, pois têm custo 1 (https://wiki.python.org/moin/TimeComplexity).

Considerando as entradas e seu processamento até a pesquisa da coordenadas (e os loopings pelos quais se passa), chegamos à fórmula C = (T-1)*(L-1)*(f-1)*(n-1)*(n-1).

<div class="math">
\begin{equation}
C(n) =
  \begin{cases}
    1 & \text{se}~n = 1 \\
    (T-1)*(L-1)*(f-1)*(n-1)*(n-1) & \text{caso contrário}
  \end{cases}
\end{equation}
</div>

Avaliando a análise do Wolfram Alpha, chegamos a conclusão que temos a complexidade O(n²).


## Outras informações que o autor julgar apropriadas para o entendimento do trabalho realizado
